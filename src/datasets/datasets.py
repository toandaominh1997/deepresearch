from typing import *
from datasets import load_dataset
from transformers import DataCollatorForLanguageModeling


def get_dataset(dataset_name: str = "tiennv/vietnamese-corpus", tokenizer: Any = None):
    data = load_dataset(dataset_name, split='train[:1%]').train_test_split(train_size = 100, test_size = 20)
    tokenizer.pad_token = tokenizer.eos_token
    def tokenize_function(examples):
        return tokenizer(examples["text"], truncation=True, max_length=512, padding="max_length")
    tokenized_datasets = data.map(tokenize_function, batched=True, remove_columns=["text"])
    data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False  # For causal language modeling
)

    # Split the dataset into training and validation sets
    train_dataset = tokenized_datasets["train"]
    eval_dataset =  tokenized_datasets["test"]
    return train_dataset, eval_dataset
