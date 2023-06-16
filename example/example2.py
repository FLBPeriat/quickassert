from typing import Union

from quickassert import *

quick_assert = new_assert()  # necessary to call once if AUTO_NEW_ASSERT is False

quick_assert['ascendant'] = lambda L: list(L) == sorted(L)
# not one optimized way to check


def enter_sorted_numbers(*numbers: Union[int, float]):
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise TypeError('numbers must int or float')
    quick_assert.ascendant('numbers', numbers)
    print('O.K.')


enter_sorted_numbers(-10, 12)
# >>> O.K.

enter_sorted_numbers(0, 1, 2, 1)
# >>> ValueError: numbers must be ascendant
