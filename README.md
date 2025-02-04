# deepresearch

## Overview

deepresearch is a deep learning research project that focuses on model training and inference using the latest AI technologies. This project is structured to facilitate easy experimentation and development with machine learning models, particularly leveraging libraries like transformers, datasets, and accelerate.

## Features

Training and inference capabilities for large language models (LLMs).
Training:
- Support reinforcement learning(PPO)

Configurable flags for controlling training and inference modes.

Utilizes transformers and datasets for dataset handling and model management.

Integration with pytest for testing functionalities.

## Requirements

This project requires Python 3.11 and the following dependencies:

see in pyproject.toml

## Installation

Using Poetry

To install the project and dependencies, run:
```
pip install poetry
poetry install
```
## Usage

### Training

To train the model, run:
```python
poetry python main.py --train_mode true --model_path "model_saved"
```

### Inference

To generate predictions:
```python
poetry python main.py --query "Your text input here" --model_path "path/to/trained/model"
```

### Running Tests

To ensure the project functions correctly, run the test suite using pytest. Tests are located in the tests/ directory.

Running All Tests

pytest

Running a Specific Test
```python

pytest
```

Running Tests with Detailed Output
```
pytest -v
```

Running Tests with Coverage Report
```
pytest --cov=src
```

### Project Structure
```
.
├── src/                # Source code for model training and inference
├── common/             # Common utilities (logger, config management)
├── tests/              # Unit tests for the project
├── main.py             # Main entry point for training and inference
├── pytest.ini          # Pytest configuration
├── pyproject.toml      # Poetry project configuration
├── poetry.lock         # Dependency lock file
├── LICENSE             # License file
├── README.md           # Project documentation
```
## License

This project is licensed under the MIT License.

## Author

Developed by Henry (toandaominh1997@gmail.com).