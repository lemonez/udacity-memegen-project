import math
import os
import time

from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """Class to hold meme-generation functionality."""

    def __init__(self, outdir):
        self.outdir = outdir
        if not os.path.isdir(outdir):
            os.mkdir(outdir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        ext = img_path.split('.')[-1]
        out_path = self.outdir + "/" + self.get_unique_filename() + '.' + ext
        with Image.open(img_path) as img:
            actual_width = img.size[0]
            if actual_width > width:
                img = self.resize_image(img, actual_width, width)
            self.add_image_quote(img, text, author)
            img.save(out_path)
        return out_path

    @staticmethod
    def resize_image(img, actual_width, width):
        # `img.size` is `(width, height)` tuple
        ratio = width/float(actual_width)
        height = int(ratio * float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)
        return img

    @staticmethod
    def add_image_quote(img, text: str, author: str) -> None:
        """Add quote to image."""
        message = f'"{text}" - {author}'
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
        draw.text((10, 30), message, font=font, fill='white')

    @staticmethod
    def get_unique_filename():
        return str(math.trunc(round(time.time(), 4) * 1000))
