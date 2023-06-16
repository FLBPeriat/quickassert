# F.L.B. Périat - 2023

from typing import Callable, Any, NoReturn, Literal, Union, Optional

from quickassert.NoAssertion import NoAssertion


class GenericAssertion(object):

    """
    Assertion admin, from which the global assertion will be raised.
    """

    def __getattribute__(self, item: Any) -> Any:
        return object.__getattribute__(self, item)

    def __setattr__(self, assertion_name: str, test: Callable[[str, Any], bool]) -> None:
        """
        Add a new assertion test under an assertion title
        :param assertion_name: name from which one will be able to call the test
        :param test: boolean test function
        :return: None
        """
        def _wrap(name: str, *args: Any, **kwargs: Any) -> Union[Literal[True], NoReturn]:
            if not test(*args, **kwargs):
                raise ValueError(f'{name} must be {assertion_name.replace("_", "")}')
            return True
        object.__setattr__(self, assertion_name, _wrap)

    def __getattr__(self, assertion_name: str) -> NoReturn:
        """
        Try to access some not instanced assertion test
        :param assertion_name: name of the assertion test
        :raise: NoAssertion: exception, because an assertion must be declared.
        """
        raise NoAssertion(assertion_name)

    def __setitem__(self, assertion_name: str, test: Callable[[Any], bool]):
        self.__setattr__(assertion_name, test)