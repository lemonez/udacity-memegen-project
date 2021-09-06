import random
import os
import requests
from flask import Flask, render_template, abort, request

from MemeGenerator import MemeEngine
from QuoteEngine.Ingestor import Ingestor

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor().parse(f))

    images_path = "./_data/photos/dog/"
    imgs = []
    for root, _, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()
print(len(quotes))
print(len(imgs))

@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice((imgs))
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme.

    If an image URL isn't specified, or if a quote or author isn't specified,
    a random stock image and/or quote is used.
    """

    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    using_stock_image = False
    img_url = request.form.get("image_url")
    if img_url in [None, ""]:
        using_stock_image = True
        img = random.choice(imgs)
        print("Using stock image")
    else:
        response = requests.get(img_url)
        img = f'./tmp/{random.randint(0,1000000)}.png'
        fo = open(img, 'wb')
        fo.write(response.content)
        fo.close()
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    body = request.form.get("body")
    author = request.form.get("author")
    if (body in [None, ""]) or (author in [None, ""]):
        quote = random.choice(quotes)
        body = quote.body
        author = quote.author
        print("Using stock quote")

    path = meme.make_meme(img, body, author)

    # # 3. Remove the temporary saved image.
    if not using_stock_image:
        os.remove(img)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
