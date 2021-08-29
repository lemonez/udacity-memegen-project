"""Module containing quote class."""


class QuoteModel:
    """Class representing a quote."""

    def __init__(self, body, author):
        """Construct quote object."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Get repr."""
        return f'{self.__class__.__name__}("{self.body}", {self.author})'

    def __str__(self):
        """Get string."""
        return f'"{self.body}" - {self.author}'
