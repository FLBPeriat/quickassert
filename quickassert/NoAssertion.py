# F.L.B. Périat - 2023


class NoAssertion(Exception):

    """
    Occurs when one try accessing one not instanced assertion in a
    generic assertion admin
    """

    def __init__(self, assertion_name: str) -> None:
        """
        Constructor of a not instanced assertion error
        :param assertion_name: printed name
        """
        super().__init__(f'no declared assertion: {assertion_name}')
