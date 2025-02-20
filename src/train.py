from typing import *
from peft import LoraConfig, get_peft_model
from trl import SFTConfig, SFTTrainer
from transformers import (
    pipeline,
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling,
)

from .datasets import get_dataset
from .models import get_model
from common import logger



def trainer_strategy(
    strategy: str,
    model_path: str,
    model: Any,
    train_dataset: Any,
    eval_dataset: Any,
    tokenizer: Any,
    data_collator: Any
):
    if strategy == "rl":
        training_args = SFTConfig(
        max_seq_length=512,
        per_device_train_batch_size=2,           
        per_device_eval_batch_size=2,   
        num_train_epochs=2,
        output_dir="/tmp/",
        report_to = "none",
        save_safetensors=False
    )

        trainer = SFTTrainer(
            model = model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset = eval_dataset,
            processing_class=tokenizer,
            data_collator=data_collator,
            
        )
    else:
        training_args = TrainingArguments(
        output_dir=model_path,      
        save_strategy="epoch",                    
        per_device_train_batch_size=2,           
        per_device_eval_batch_size=2,             
        num_train_epochs=2,                       # Number of epochs
        learning_rate=5e-5,                       # Learning rate
        weight_decay=0.01,                        # Weight decay
        save_total_limit=2,                       # Save only the 2 most recent models
        fp16=False,                                # Enable mixed precision
        logging_dir="./logs",                     # Logging directory
        logging_steps=500,                        # Log every 500 steps
        report_to="none", 
        save_safetensors=False
    )
        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            processing_class=tokenizer,
            data_collator=data_collator
        )

    return trainer


def training(
    model_path: str = "./model_saved"
):
    
    model, tokenizer = get_model()

    train_dataset, eval_dataset = get_dataset(tokenizer=tokenizer)
    data_collator = DataCollatorForLanguageModeling(
        tokenizer = tokenizer,
        mlm = False
        
    )

    trainer = trainer_strategy(
        strategy="rl",
        model_path=model_path,
        model = model,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        tokenizer=tokenizer,
        data_collator=data_collator
    )

    logger.info("Start training ...")
    trainer.train()

    logger.info(f"Save model: {model_path}")
    trainer.save_model(model_path)
    logger.info(f"Save tokenizer: {model_path}")
    tokenizer.save_pretrained(model_path)
    logger.info(f"Model training completed! Model saved: {model_path}")
    return True

