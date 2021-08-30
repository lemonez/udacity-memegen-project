"""Module for ingesting CSV files."""
import csv
# TODO: Must I used pandas? I'd think that using vanilla Python would be preferable since it's harder.

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Class for ingesting CSV files."""

    allowed_extensions = ["csv"]

    @classmethod
    def parse(cls, path="../_data/DogQuotes/DogQuotesCSV.csv"):
        """Parse quote file."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest this file type')
        quotes = []
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            for line in reader:
                quotes.append(line)

        quote_models = []
        for quote in quotes:
            qm = QuoteModel(quote['body'], quote['author'])
            quote_models.append(qm)

        return quote_models
