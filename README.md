# timer example package

## Installation

Install this module with pip (requires Python 3.8 or newer)

```sh
pip install -U git+https://github.com/nobeam/example-package-timer
```

## Usage

Just put a decorator on top of your function and it will print the elapsed time every time you call it.

```python
from timer import timer

@timer
def your_function()
    ...

```
