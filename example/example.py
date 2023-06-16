
from quickassert import *

entry_assert = new_assert(_global=False)  # necessary to call once if AUTO_NEW_ASSERT is False

# declare assertion test named digit
entry_assert['digit'] = lambda x: 0 <= x < 10


def enter_digit(d: int) -> None:
    if isinstance(d, int):
        entry_assert.digit('d', d)
        print('O.K.')
        return
    raise TypeError('d must be int')


enter_digit(4)
# >>> O.K.

enter_digit(23)
# >>> ValueError: d must be digit
