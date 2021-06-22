# Cool python libraries

This repositroy demonstrates some of very useful python libraries

Inspired by this [video](https://www.youtube.com/watch?v=eILeIEE3C8c)

## 1) Argh

As the [docs](https://argh.readthedocs.io/en/latest/) says:

Argh is a smart wrapper for argparse. Argparse is a very powerful tool; Argh just makes it easy to use.

### Argh installation

```bash
pip install argh
```

### Argh usage
Code snippets for this module can be found in directory "argh".

For example, a calculator created using argh:
```python
import argh



def calc(expr):
    print(f'Evaluating expression {expr}')
    try:
        return eval(expr)
    except:
        return 'Given algebraic expression is invalid'


if __name__ == '__main__':
    argh.dispatch_command(calc)
```
```html
cd argh

python calc.py -h
    usage: calc.py [-h] expr

    positional arguments:
    expr        -

    optional arguments:
    -h, --help  show this help message and exit


python calc.py 5+5
    Evaluating expression 5+5
    10


python calc.py 2+2*2
    Evaluating expression 2+2*2
    6
```
## 2) Tqdm

As the [docs](https://tqdm.github.io/) says:

Tqdm instantly makes your loops show a smart progress meter - just wrap any iterable with `tqdm(iterable)`, and you’re done!

### Tqdm installation

```bash
pip install tqdm
```

### Tqdm usage
Code snippets for this module can be found in directory "tqdm".

For example, basic tqdm usage:
```python
from tqdm import tqdm
from time import sleep

a = 0

for i in tqdm(range(100)):
    a += i
    sleep(0.1)

print(a)
```
```bash
cd tqdm

python quickstart.py
100%|█████████████████████████████████████████████████████████████| 100/100 [00:10<00:00,  9.86it/s] 
4950
```
## 3) Typing

Typing forces Python to be strongly-typed language (in combination with mypy).
This module provides with a variety of types for type hints: `Any, Callable, Union, Dict, List, Iterable, Literal` and so on.

As the [Docs](https://docs.python.org/3/library/typing.html) 

### Typing installation

```bash
No need to install
```

### Typing usage
Code snippets for this module can be found in directory "typing".

For example, functions that accept some types:
```python
def factorial(n: Union[int, float]) -> int:

    # Because None is ignored, we have to create None validation on our own:
    if n is None:
        return 0

    n = int(n)

    if n < n:
        return 0
    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(3.5))
print(factorial('5'))

'''
python -m mypy quickstart.py

Outputs an error:
error: Argument 1 to "factorial" has incompatible type "str"; expected "int"
Found 1 error in 1 file (checked 1 source file)
'''

def map_int_list(fn: Callable, l: List[int]) -> List[int]:
    return [fn(e) for e in l]

print(map_int_list(factorial, [0, 1, 2, 3, 4]))


def map_int_dict(fn: Callable, d: Dict[Any, int]) -> Dict[Any, int]:
    return {key: fn(value) for key, value in d.items()}

print(map_int_dict(factorial, {'a': 1, 'b': 5, 'c': 4, 'j': 9}))
```