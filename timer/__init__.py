__version__ = "0.1.0"

from typing import Callable
from time import process_time
from colorama import Fore


def timer(function: Callable):
    def wrapper(*args, **kwargs):
        time = process_time()
        result = function(*args, **kwargs)
        print(f"{Fore.BLUE}Elasped time {process_time() - time:.3f} s{Fore.RESET}")
        return result + 1

    return wrapper
