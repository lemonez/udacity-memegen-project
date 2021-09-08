"""Module for generating memes, with MemeEngine class."""

import math
import os
import random
import time

from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """Class to hold meme-generation functionality."""

    def __init__(self, outdir):
        """Construct MemeEngine instance method."""
        self.outdir = outdir
        if not os.path.isdir(outdir):
            os.mkdir(outdir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a meme."""
        ext = img_path.split('.')[-1]
        out_path = self.outdir + "/" + self.create_unique_filename() + '.' + ext
        with Image.open(img_path) as img:
            actual_width = img.size[0]
            if actual_width > width:
                img = self.resize_image(img, actual_width, width)
            self.add_image_quote(img, text, author)
            img.save(out_path)
        return out_path

    @staticmethod
    def resize_image(img, actual_width, width):
        """Resize an image."""
        # `img.size` is `(width, height)` tuple
        ratio = width/float(actual_width)
        height = int(ratio * float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)
        return img

    @staticmethod
    def add_image_quote(img, text: str, author: str) -> None:
        """Add quote to an image."""
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)

        if (len(text) > 20):
            # insert newline every fifth space
            with_newlines = ''
            spaces = 0
            for character in text:
                if character == ' ':
                    spaces += 1
                    # will be 1 the first time, so won't prepend newline at start
                    if spaces % 5 == 0:
                        with_newlines += '\n'
                    else:
                        with_newlines += character
                else:
                    with_newlines += character
            message = f'"{with_newlines}"\n  - {author}'
        else:
            message = f'"{text}" - {author}'
        draw.text((random.randint(1,30), random.randint(1,50)), message, font=font, fill='purple')

    @staticmethod
    def create_unique_filename():
        """Create a unique temp filename for the meme."""
        return str(math.trunc(round(time.time(), 4) * 1000))
