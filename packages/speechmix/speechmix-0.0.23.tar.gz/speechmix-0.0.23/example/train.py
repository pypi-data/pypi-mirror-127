import argparse
import os
import sys

import asrp

import speechmix
from datasets import load_dataset, Audio, load_from_disk
import torch
from transformers import Wav2Vec2Processor, Trainer, TrainingArguments, EarlyStoppingCallback
from typing import Dict, List, Union, Optional
from dataclasses import dataclass


def main(arg=None):
    def prepare_dataset(batch):
        audio = batch["audio"]
        batch["input_values"] = model.processor(audio["array"], sampling_rate=16_000).input_values[0]
        batch["length"] = batch["input_values"].size
        sent = batch["text"] if 'text' in batch else batch["sentence"]
        batch["labels"] = model.tokenizer(sent).input_ids[1:]
        batch["input_ids"] = batch["labels"]
        return batch

    def compute_metrics(pred):
        pred_ids = pred.predictions
        pred_ids = [i[i != -100] for i in pred_ids]
        pred_str = model.tokenizer.batch_decode(pred_ids, skip_special_tokens=True, group_tokens=False)
        # we do not want to group tokens when computing the metrics
        label_ids = pred.label_ids
        label_ids = [i[i != -100] for i in label_ids]
        label_str = model.tokenizer.batch_decode(label_ids, skip_special_tokens=True, group_tokens=False)

        cer = asrp.cer(label_str, pred_str)
        wer = asrp.wer(label_str, pred_str)
        return {"cer": cer, "wer": wer}

    @dataclass
    class DataCollatorWithPadding:
        processor: Wav2Vec2Processor
        tokenizer: Wav2Vec2Processor
        padding: Union[bool, str] = True
        max_length: Optional[int] = None
        max_length_labels: Optional[int] = None
        pad_to_multiple_of: Optional[int] = None
        pad_to_multiple_of_labels: Optional[int] = None
        selftype: bool = False

        def __call__(self, features: List[Dict[str, Union[List[int], torch.Tensor]]]) -> Dict[str, torch.Tensor]:
            # split inputs and labels since they have to be of different lenghts and need
            # different padding methods
            input_features = [{"input_values": feature["input_values"]} for feature in features]
            label_features = [{"input_ids": feature['labels']} for feature in features]

            batch = self.processor.pad(
                input_features,
                padding=self.padding,
                max_length=self.max_length,
                pad_to_multiple_of=self.pad_to_multiple_of,
                return_tensors="pt",
            )

            labels_batch = self.tokenizer.pad(
                label_features,
                padding=self.padding,
                max_length=self.max_length_labels,
                pad_to_multiple_of=self.pad_to_multiple_of_labels,
                return_tensors="pt",
            )

            if self.selftype:
                labels_batch = labels_batch['input_ids']
            else:
                labels_batch = labels_batch['input_ids'].masked_fill(labels_batch.attention_mask.ne(1), -100)
            batch['labels'] = labels_batch
            return batch

    def parse_args(args):
        parser = argparse.ArgumentParser()
        parser.add_argument("--speech_model_config", type=str)
        parser.add_argument("--nlp_model_config", type=str)
        parser.add_argument("--SpeechMixEED", action='store_true')
        parser.add_argument("--SpeechMixED", action='store_true')
        parser.add_argument("--SpeechMixSelf", action='store_true')
        parser.add_argument("--SpeechMixGAN", action='store_true')
        parser.add_argument("--dataset", type=str)
        parser.add_argument("--field", type=str)
        parser.add_argument("--train_split", type=str)
        parser.add_argument("--test_split", type=str)
        parser.add_argument("--grad_accum", default=3, type=str)
        parser.add_argument("--batch", type=int)
        parser.add_argument("--ftl", action='store_true')
        parser.add_argument("--lna", action='store_true')
        parser.add_argument("--lnae", action='store_true')
        parser.add_argument("--fne", action='store_true')

        input_arg, model_arg = parser.parse_known_args(args)
        input_arg = {k: v for k, v in vars(input_arg).items() if v is not None}
        other_arg = {k.replace("--", ""): v for k, v in zip(model_arg[:-1:2], model_arg[1::2])}
        return input_arg, other_arg

    input_arg, other_arg = parse_args(sys.argv[1:]) if arg is None else parse_args(arg)
    print("input_arg", input_arg)

    if input_arg['SpeechMixEED']:
        model_type = "SpeechMixEED"
        if input_arg['lna']:
            model_type += "_lna"
        elif input_arg['lnae']:
            model_type += "_lnae"
        elif input_arg['fne']:
            model_type += "_fne"
        model = speechmix.SpeechMixEED(input_arg['speech_model_config'], input_arg['nlp_model_config'],
                                       lna=input_arg['lna'], lnae=input_arg['lnae'], fne=input_arg['fne'])
    elif input_arg['SpeechMixSelf']:
        model_type = "SpeechMixSelf"
        model = speechmix.SpeechMixSelf(input_arg['speech_model_config'], input_arg['nlp_model_config'])
    elif input_arg['SpeechMixGAN']:
        model_type = "SpeechMixGAN"
        model = speechmix.SpeechMixGAN(input_arg['speech_model_config'], input_arg['nlp_model_config'])
    else:
        model_type = "SpeechMixED"
        if input_arg['ftl']:
            model_type += "_ftl"
        model = speechmix.SpeechMixED(input_arg['speech_model_config'], input_arg['nlp_model_config'],
                                      ftl=input_arg['ftl'])

    cache_path_train = f'./train_ds_{input_arg["dataset"]}_{input_arg["field"]}_{input_arg["train_split"]}.parquet'
    cache_path_valid = f'./valid_ds_{input_arg["dataset"]}_{input_arg["field"]}_{input_arg["train_split"]}.parquet'

    if os.path.exists(cache_path_train) and os.path.exists(cache_path_valid):
        train_ds = load_from_disk(cache_path_train)
        valid_ds = load_from_disk(cache_path_valid)
    else:
        train_ds = load_dataset(input_arg["dataset"], input_arg["field"], split=input_arg["train_split"])
        valid_ds = load_dataset(input_arg["dataset"], input_arg["field"], split=input_arg["test_split"])

        train_ds = train_ds.cast_column("audio", Audio(sampling_rate=16_000))
        valid_ds = valid_ds.cast_column("audio", Audio(sampling_rate=16_000))

        train_ds = train_ds.map(prepare_dataset, num_proc=1, )
        valid_ds = valid_ds.map(prepare_dataset, num_proc=1, )

        train_ds.save_to_disk(cache_path_train)
        valid_ds.save_to_disk(cache_path_valid)

    data_collator = DataCollatorWithPadding(processor=model.processor, tokenizer=model.tokenizer, padding=True,
                                            selftype=(model_type == 'SpeechMixSelf'))

    training_args = TrainingArguments(
        output_dir=f"./{input_arg['speech_model_config']}_{input_arg['nlp_model_config']}_{model_type}",
        per_device_train_batch_size=int(input_arg['batch']),
        per_device_eval_batch_size=int(input_arg['batch']),
        gradient_accumulation_steps=int(input_arg['grad_accum']),
        eval_accumulation_steps=2,
        evaluation_strategy="steps",
        group_by_length=True,
        load_best_model_at_end=True,
        num_train_epochs=1000,
        fp16=True,
        save_steps=500,
        eval_steps=500,
        logging_steps=100,
        learning_rate=6e-4,
        warmup_steps=500,
        save_total_limit=2,
        dataloader_num_workers=10,
    )
    # some trainer problem - save all logistics on compute_metrics, cause out of memory, fix:argmax first;
    # dynamic padding on past key value, cause index error, fix: return only loss and logist
    # group_by_length took lots of time during preprocessing
    trainer = Trainer(
        model=model,
        args=training_args,
        compute_metrics=compute_metrics,
        train_dataset=train_ds,
        eval_dataset=valid_ds,
        data_collator=data_collator,
        tokenizer=model.tokenizer,
        callbacks=[EarlyStoppingCallback(early_stopping_patience=20)]
    )

    trainer.train()
    trainer.predict(train_ds)


if __name__ == "__main__":
    main()
