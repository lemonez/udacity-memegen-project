"""Module for ingesting PDF files."""
import os
import random
import subprocess

from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Class for ingesting PDF files."""

    allowed_extensions = ["pdf"]

    @classmethod
    def parse(cls, path="../_data/DogQuotes/DogQuotesPDF.pdf"):
        """Parse quote file."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest this file type')
        tmp = f'../_data/tmp/{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        quotes = []
        with open(tmp, 'r') as f:
            for line in f.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    elems = line.split(' "')
                    for elem in elems:
                        body, author = elem.replace('"', "").split(' - ')
                        quotes.append({"body": body, "author": author})
        quote_models = []
        for quote in quotes:
            qm = QuoteModel(quote["body"], quote["author"])
            quote_models.append(qm)

        return quote_models
