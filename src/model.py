from typing import *
from transformers import (
    pipeline,
    AutoTokenizer,
    AutoModelForCausalLM
)
from peft import LoraConfig, get_peft_model
from common import logger


def get_model(model_name: str="Qwen/Qwen2.5-1.5B"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    logger.info(f"""
MEMORY_FOOTPRINT: {model.get_memory_footprint()}
""")
    lora_config = LoraConfig(
        r=16,  # Rank of the LoRA matrices
        lora_alpha=32,  # Scaling factor
        target_modules=["lm_head",],  # Modules to apply LoRA (e.g., attention weights)
        lora_dropout=0.1,  # Dropout rate
        bias="none",  # Bias strategy
        task_type="CAUSAL_LM"  # Task type (e.g., Causal LM, Seq2Seq)
    )
    model = get_peft_model(model, lora_config)
    logger.info(f"trainable parameters: {model.print_trainable_parameters()}")
    return model, tokenizer
