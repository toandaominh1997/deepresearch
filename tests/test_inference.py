from main import training, prediction
from common import Flags, logger
def test_inference():
    Flags.create("model_path", "model_saved", "Model path")
    Flags.create("train_mode", False, "Training mode")
    Flags.create("query", "Hello", "Query to LLM model")
    Flags.parse()
    logger.info(f"Config: {Flags.getParse()}")

    logger.info("Start deepresearch ...")
    if Flags.get("train_mode"):
        training(model_path = Flags.get("model_path"))
        return 0
    
    prediction(Flags.get("query"))
    