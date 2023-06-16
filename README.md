# quickassert

A Python runtime service:
Assertion admin with generated exception

## Short Description from v.1.0 (first)

Creates assertion administor (access) on relatively small prodjects, in order to save time used in raising and writing exceptions.
It generate automatically a one-pattern exception.

## Quick Use

First, run the command:

``pip install quickassert``

When the installation is done, an example is:

```
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
```

where one can obtain:


```
>>> enter_digit(4)
>>> O.K.

>>> enter_digit(23)
>>> ValueError: d must be digit
```

## Coming in following versions

* Better exception and message handling.
* Mode with inspection, no need to pass variable name if same (maybe with a decorator)
* Smallest tree checking, for optimisation, for example:
    (x > 3) & (x > 5) ~ (x > 5)
* Typing check adapted.
* And maybe more

