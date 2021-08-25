class QuoteModel:
    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.body}", {self.author})'

    def __str__(self):
        return f'"{self.body}" -{self.author}'
