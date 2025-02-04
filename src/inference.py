from typing import *
from transformers import (
    pipeline,
    AutoTokenizer,
    AutoModelForCausalLM
)
from common import time_response, logger

@time_response
def model_prediction(query: str, pipeline: pipeline):
    return pipeline(query)
def inference(
    query: str = "Hi",
    model_path: str = "model_saved/"):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)

    llm_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)
    logger.info("Model prediction ... ")
    output = model_prediction(query, pipeline=llm_pipeline)
    return output
    
