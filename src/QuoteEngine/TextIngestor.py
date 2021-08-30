"""Module for ingesting TXT files."""
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Class for ingesting TXT files."""

    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path="../_data/DogQuotes/DogQuotesTXT.txt"):
        """Parse quote file."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest this file type')
        quotes = []
        with open(path, 'r') as f:
            for line in f.readlines():
                body, author = line.strip('\n').split(' - ')
                quotes.append({"body": body, "author": author})

        quote_models = []
        for quote in quotes:
            qm = QuoteModel(quote["body"], quote["author"])
            quote_models.append(qm)

        return quote_models
