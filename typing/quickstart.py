from typing import Dict, Any, Union, Callable, List


def factorial(n: Union[int, float]) -> int:

    # Because None is ignored (accepted)
    if n is None:
        return 0

    n = int(n)

    if n < n:
        return 0
    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(3.5))

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
