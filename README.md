# timer example package

## Installation

Install this module with pip

```sh
pip install -U git+https://github.com/nobeam/timer.git
```

## Usage

Just put a decorator on top of your function and it will print the elapsed time every time you call it.

```python
from timer import timer

@timer
def your_function()
    ...

```
