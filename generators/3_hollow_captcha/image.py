# coding: utf-8
import os
import random
from PIL import Image, ImageChops
from PIL.ImageDraw import Draw
from PIL.ImageFont import truetype
try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO
try:
    from wheezy.captcha import image as wheezy_captcha
    from wheezy.captcha.comp import getrgb
except ImportError:
    wheezy_captcha = None

DATA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')
DEFAULT_FONTS = ['DroidSansMono.ttf']

if wheezy_captcha:
    __all__ = ['WheezyCaptcha']




class _Captcha(object):
    def generate(self, chars, font_size=None, format="png"):
        """Generate an Image Captcha of the given characters.

        :param chars: text to be generated.
        :param format: image file format
        """
        im = self.generate_image(chars, font_size)
        out = BytesIO()
        im.save(out, format=format)
        out.seek(0)
        return out
    def generate_dbg(self, chars, font_size=None):
        im = self.generate_image(chars, font_size)
        return im
    def __del__(self):
        pass


class WheezyCaptcha(_Captcha):
    """Create an image CAPTCHA with wheezy.captcha."""
    def __init__(self, width=220, height=45, fonts=None, font_sizes=[30, 50, 70], squeeze_factor=0.5, border=2):
        self._width = width
        self._height = height
        self._fonts = fonts or DEFAULT_FONTS
        self.font_sizes = font_sizes
        self.squeeze_factor = squeeze_factor
        self.border = border
    def __del__(self):
        pass
    def _outline(self, draw, dx, dy, c, font, color, border=2):
        draw.text((dx - border, dy), c, font=font, fill=color)
        draw.text((dx + border, dy), c, font=font, fill=color)
        draw.text((dx, dy - border), c, font=font, fill=color)
        draw.text((dx, dy + border), c, font=font, fill=color)
        
        draw.text((dx - border, dy - border), c, font=font, fill=color)
        draw.text((dx + border, dy - border), c, font=font, fill=color)
        draw.text((dx - border, dy + border), c, font=font, fill=color)
        draw.text((dx + border, dy + border), c, font=font, fill=color)
    def _remove_white_background_with_chops(self, img):
        fuzz = 2  # Choose a value greater than 0. Play around for optimal results.
        bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
        diff = ImageChops.difference(img, bg)
        diff = ImageChops.add(diff, diff, fuzz, -100)
    
        W, H = img.size
        for x in range(W):
            for y in range(H):
                if diff.getpixel((x, y)) == (0, 0, 0, 0):
                    # Make transparent.
                    # Now making grey to easier show on screen that it works.
                    img.putpixel((x, y), (0, 0, 0))
#                     img.putpixel((x, y), (128, 128, 128))
    def text(self, fonts, font_sizes=None, drawings=None, color='#FFFFFF',
             squeeze_factor=0.5, border=2, b_color="#000000"):
        fonts = tuple([truetype(name, size)
                       for name in fonts
                       for size in font_sizes or (65, 70, 75)])
        if not callable(color):
            c = getrgb(color)
    
            def color():
                return c
        if not callable(b_color):
            bc = getrgb(b_color)
    
            def b_color():
                return bc
        def drawer(image, text):
            draw = Draw(image)
            char_images = []
            for c in text:
                font = random.choice(fonts)
                c_width, c_height = draw.textsize(c, font=font)
                char_image = Image.new('RGBA', (c_width + 1, c_height + 1), "black")
                char_draw = Draw(char_image)
                self._outline(char_draw, 0, 0, c, font, "gray", border)
                char_draw.text((0, 0), c, font=font, fill="black")
                
                
                char_image = char_image.crop(char_image.getbbox())
                for drawing in drawings:
                    char_image = drawing(char_image)
                char_image = char_image.resize((char_image.width, 42))
                char_images.append(char_image)
            width, height = image.size
            offset = int((width - sum(int(i.size[0] * squeeze_factor)
                                      for i in char_images[:-1]) - 
                          char_images[-1].size[0]) / 2)
            for char_image in char_images:
                c_width, c_height = char_image.size
                mask = char_image.convert('L').point(lambda i: i * 1.97)
                image.paste(char_image,
                            (offset, int((height - c_height) / 2)),
                            mask)
                offset += int(c_width * squeeze_factor)
            self._remove_white_background_with_chops(image)
            return image
        return drawer    
    def generate_image(self, chars, font_size=None):
        text_drawings = [
            wheezy_captcha.warp(),
            wheezy_captcha.rotate(),
            wheezy_captcha.offset(dx_factor=0.1, dy_factor=0.0),
        ]
        if font_size is not None:
            self.font_sizes = [font_size]
        fn = wheezy_captcha.captcha(
            drawings=[
                wheezy_captcha.background(color="#FFFFFF"),
                self.text(fonts=self._fonts, drawings=text_drawings, font_sizes=self.font_sizes, squeeze_factor=self.squeeze_factor, border=self.border),
#                 wheezy_captcha.curve(),
#                 wheezy_captcha.noise(),
#                 wheezy_captcha.smooth(),
            ],
            width=self._width,
            height=self._height,
        )
        return fn(chars).convert('L')



def random_color(start, end, opacity=None):
    red = random.randint(start, end)
    green = random.randint(start, end)
    blue = random.randint(start, end)
    if opacity is None:
        return (red, green, blue)
    return (red, green, blue, opacity)
