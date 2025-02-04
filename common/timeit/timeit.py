from typing import *
from functools import wraps
import time


def time_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()          # Record start time
        result = func(*args, **kwargs)    # Execute the function
        end_time = time.time()            # Record end time
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {elapsed_time:.6f} seconds")
        return result
    return wrapper


