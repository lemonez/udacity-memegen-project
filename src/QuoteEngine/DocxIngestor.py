import docx

from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):

    allowed_extensions = ["docx"]

    @classmethod
    def parse(cls, path="../_data/DogQuotes/DogQuotesDOCX.docx"):
        if not cls.can_ingest(path):
            raise Exception('cannot ingest this file type')
        quotes = []
        doc = docx.Document(path)
        for line in doc.paragraphs:
            if line.text != "":
                body, author = line.text.strip('\n').split(' - ')
                # remove extra double quotes in parsed quote string
                body = body.replace('"', "")
                quotes.append({"body": body, "author": author})

        quote_models = []
        for quote in quotes:
            qm = QuoteModel(quote["body"], quote["author"])
            quote_models.append(qm)

        return quote_models
