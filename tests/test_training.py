import pytest
from common import Flags
from main import training

def test_training():
    Flags.create("model_path", "model_saved", "Model path")
    Flags.create("train_mode", True, "Training mode")
    Flags.create("query", "Hello", "Query to LLM model")
    Flags.parse()

    if Flags.get("train_mode"):
        training(model_path = Flags.get("model_path"))

