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

from common import Flags, logger, timeit
from src.train import training
from src.inference import inference

def prediction(query):
    outputs = inference(query=query,
    model_path = Flags.get("model_path")
    )
    response = '\n\n'.join([output['generated_text'] for output in outputs])
    print(f"""
Query: {query}   
output: {response}
""")

def solve():
    Flags.create("model_path", "model_saved", "Model path")
    Flags.create("train_mode", False, "Training mode")
    Flags.create("query", "Say hello to me", "Query to LLM model")
    Flags.parse()
    logger.info(f"Config: {Flags.getParse()}")

    logger.info("Start deepresearch ...")
    if Flags.get("train_mode"):
        training(model_path = Flags.get("model_path"))
        return 0
    
    prediction(Flags.get("query"))
    


if __name__ == '__main__':
    solve()