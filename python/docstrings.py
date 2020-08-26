"""
Description for document module

See how the Docstring automatically creates documents:
help(docstrings.py)
help(double)
help(D)

Validate examples within docstrings
pytest docstrings.py

Examples:
    >>> d = D(2)
    >>> d.double() == double(2)
    True
"""

def double(n: int) -> int:
    """
    Function Docstring - Description
    Arguments:
        n: an integer
    Returns:
        n * 2
    Examples:
        >>> double(2)
        4
    """
    return n * 2

class D:
    """
    Class Docstring - Description
    Arguments:
        n: an integer
    Attributes:
        n: an integer
    """

    def __init__(self, n: int):
        self.n = n

    def double(self):
        """
        Method Docstring - Description
        Returns:
            2 * n
        """
        return self.n * 2