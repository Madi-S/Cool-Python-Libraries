
from typing import Any, Iterable, List, Literal, NoReturn, Optional, Set, Union, Tuple, Callable, TypeVar, Generic, Sequence

# Basics


def get_type(obj: Any):
    return type(obj).__name__


print(get_type(23))
print(get_type('Greetings!'))
print(get_type({42: 'Nice'}))

Array = TypeVar('Array', Tuple, List, Set)


def get_length(a: Array):
    return len(a)


print(get_length([2, 4, 42]))
print(get_length((2, 4, 42)))
print(get_length({2, 4, 42}))

# Aliases
Coordinates = Tuple[float, int]


def get_formatted_position(c: Coordinates) -> str:
    return f'X: {c[0]}, Y: {c[1]}'


get_formatted_position((2.3, 5))


# Callable

S = TypeVar('S', Tuple[int], List[int], Set[int]) or Iterable[int]


def map_list(s: S, fn: Callable[[int], Any]) -> S:
    return map(fn, s)

# NoReturn and Optional


def say_smth(smth: Optional[str] = 'something') -> NoReturn:
    print('Saying', smth)

# Literal


MODE = Literal['r', 'rb', 'w', 'wb']


def open_helper(file: str, mode: MODE) -> str:
    ...

open_helper('/some/path', 'r')      # Passes type check
open_helper('/other/path', 'typo')  # Error in type checker