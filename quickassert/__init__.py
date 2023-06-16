# F.L.B. Périat - 2023

from quickassert.GenericAssertion import GenericAssertion


quick_assert: GenericAssertion = None


def new_assert(_global: bool = True) -> GenericAssertion:
    if _global:
        global quick_assert
        if quick_assert is None:
            quick_assert = GenericAssertion()
        return quick_assert
    return GenericAssertion()


AUTO_NEW_ASSERT: bool = False  # modify here with True if needed
"""
    Creates an global instance of assertion admin
"""

if AUTO_NEW_ASSERT:
    new_assert()
