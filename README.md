# Meme Generator

The meme generator reads quotes in various file types and prints them on an image. If you supply a quote and/or path to image at the command line, that will get printed on an image instead. Otherwise, a random image and quote will be used.

## Files included

The project includes a `QuoteEngine` directory, which contains several `*Ingestor*` modules, which are responsible for handling the ingestion of quotes of various formats.

The `MemeGenerator` module is responsible for generating memes given photos and quotes.

The `meme` module handles the generation of memes.

The `app` module handles the Flask app, calling the other modules to generate memes.

## Running the program at the command line

At the command line, you can run `Python meme.py -h` to get the help menu.

The program takes three OPTIONAL arguments:

- A string quote body
- A string quote author
- An image path

If one of these arguments isn't supplied, it'll draw a random one from the built-in images and quotes.

## Running the program through a browser

This program is wrapped up in a Flask app. To start the server, run `python app.py`.

To use the app, navigate to the URL that it specifies in the terminal output; likely it'll be something like `http://127.0.0.0:5000/`.