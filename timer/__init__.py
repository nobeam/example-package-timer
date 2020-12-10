__version__ = "0.1.0"

from time import process_time
from colorama import Fore


def timer(function):
    def wrapper(*args, **kwargs):
        time = process_time()
        result = function(*args, **kwargs)
        print(f"{Fore.BLUE}Elasped time {process_time() - time:.3f} s{Fore.RESET}")
        return result

    return wrapper
