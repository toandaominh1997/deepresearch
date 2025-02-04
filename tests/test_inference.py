from main import training, prediction
from common import Flags, logger
def test_inference():
    Flags.create("model_path", "Qwen/Qwen2.5-1.5B", "Model path")
    Flags.create("train_mode", False, "Training mode")
    Flags.create("query", "Hello", "Query to LLM model")
    Flags.parse()
    logger.info(f"Config: {Flags.getParse()}")
    prediction(Flags.get("query"))
    