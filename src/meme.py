"""Module to parse meme args and generate meme."""

import argparse
import os
import random

from QuoteEngine import Ingestor, QuoteModel
from MemeGenerator import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given a path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, _, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.Ingestor().parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel.QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse meme-related args.")
    parser.add_argument("-p", dest="path",
                        help="path to an image file")
    parser.add_argument("-b", dest="body",
                        help="quote body to add to the image")
    parser.add_argument("-a", dest="author",
                        help="quote author to add to the image")
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
