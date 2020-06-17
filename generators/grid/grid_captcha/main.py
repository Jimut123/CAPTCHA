import io
import random
import string
import pkg_resources
from base64 import b64encode

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy.ndimage.filters import gaussian_filter


class CaptchaBuilder:
    def __del__(self):
        # body of destructor
        pass
    def __init__(self):

        # General
        self._symbol_height = 5
        self._size = (325, 63)
        self._color = lambda: (random.randint(100, 150), random.randint(125, 200), random.randint(125, 200))

        # Symbols
        self._fonts = []
        for f in pkg_resources.resource_listdir('grid_captcha', 'fonts'):
            self._fonts.append(ImageFont.truetype(pkg_resources.resource_filename('grid_captcha', f'fonts/{f}'), 55))

        self._symbols = ''.join(i for i in (string.ascii_letters + string.digits) if i not in 'QCGIJORUVaecijloruv01')

        # Distortion
        self._sigma = 8
        self._alpha = lambda: random.randint(150, 200)

        # build()
        self.word = None
        self._image = None
        self._image_draw = None
        self._pixels = None

        # _grid_gen()
        self._grid_x = None
        self._grid_y = None
        self._len_grid_x = None
        self._len_grid_y = None

    def _grid_gen(self):
        """Generates the coordinates of the beginning of lines for each axis."""

        y = 0
        self._grid_y = []
        while y <= self._size[1]:
            self._grid_y.append(y)
            y += random.randint(2, 3)

        x = 0
        self._grid_x = []
        while x <= self._size[0]:
            self._grid_x.append(x)
            x += random.randint(3, 4)

        self._len_grid_x = len(self._grid_x)
        self._len_grid_y = len(self._grid_y)

    def _draw_lines_from_symbols(self):
        """Draws symbols. Erases all lines except the grid lines."""

        font = random.choice(self._fonts)

        # maximum distance between characters
        max_x_add = int((self._size[0] - sum([font.getsize(symbol)[0] for symbol in self.word])) / 5)

        # First indent
        x = random.randint(0, max_x_add)

        # Draw characters with random x and y (within reason)
        for i in range(len(self.word)):
            (_, height), (_, offset_y) = font.font.getsize(self.word[i])
            y_add = random.randint(int(self._symbol_height * 1.5), self._size[1] - height - self._symbol_height)
            self._image_draw.text((x, y_add - offset_y), self.word[i], fill=(0, 0, 0), font=font)
            x += font.getsize(self.word[i])[0] + random.randint(5, max_x_add)

        # Erase all lines except those in grid_y
        for y in [item for item in [i for i in range(63)] if item not in self._grid_y]:
            self._image_draw.line((0, y, self._size[0], y), fill='white')

    def _erase_symbols_lines(self):
        """Erases lines from the characters."""

        for y in range(self._len_grid_y - 1):
            for x in range(self._len_grid_x - 1):
                for i in range(self._grid_x[x + 1] - self._grid_x[x]):
                    self._pixels[self._grid_x[x] + i, self._grid_y[y]] = (255, 255, 255)

    def _calc_y_for_horizontal_lines(self):
        """Calculates y coordinates for each horizontal line based on characters and distortion."""

        # Coordinate difference for applying distortion
        distortion = (gaussian_filter((np.random.rand(self._len_grid_x, len(self._grid_y)) * 2 - 1),
                                      self._sigma, mode="constant", cval=0) * self._alpha()).astype(int)

        # Fill with standard values to avoid errors at the borders of the image
        horizontal_lines_y = [[0 for _ in range(len(self._grid_x))] for _ in range(len(self._grid_y))]
        for y in range(len(self._grid_y)):
            for x in range(len(self._grid_x)):
                horizontal_lines_y[y][x] = self._grid_y[y]

        # Calculate coordinates
        for y in range(self._len_grid_y - 1):
            for x in range(self._len_grid_x - 1):

                add = - int(distortion[x, y])

                # If there are lines from symbols on the left and right =>
                # adding the height of characters to the difference
                if self._pixels[self._grid_x[x] + 1, self._grid_y[y]] != (255, 255, 255) and \
                        self._pixels[self._grid_x[x] - 1, self._grid_y[y]] != (255, 255, 255):
                    add -= self._symbol_height

                horizontal_lines_y[y][x] = self._grid_y[y] + add

        # Correct the distortion at the last x-axis coordinates
        for y in range(len(self._grid_y)):
            for x in range(self._len_grid_x - 1, len(self._grid_x)):
                add = - int(distortion[x, y])
                horizontal_lines_y[y][x] = self._grid_y[y] + add

        self._erase_symbols_lines()  # We no longer need symbol lines

        return horizontal_lines_y

    def _draw_grid(self):
        """Draws a grid based on distortion and symbols"""

        horizontal_lines_y = self._calc_y_for_horizontal_lines()

        # Generate new color
        color = self._color()

        # Draw vertical lines
        for y in range(self._len_grid_y - 1):
            for x in range(self._len_grid_x - 1):

                coords = (self._grid_x[x], horizontal_lines_y[0][x], self._grid_x[x], horizontal_lines_y[-2][x])
                self._image_draw.line(coords, fill=color)

        # Draw horizontal lines
        for y in range(self._len_grid_y - 1):
            for x in range(self._len_grid_x - 1):

                # If we go higher or lower due to distortion => r + 25, g + 25, b + 25
                if abs(horizontal_lines_y[y][x + 1] - horizontal_lines_y[y][x]) == 1:
                    fill_color = (color[0] + 25, color[1] + 25, color[2] + 25)
                else:
                    fill_color = color

                coords = (self._grid_x[x], horizontal_lines_y[y][x], self._grid_x[x + 1], horizontal_lines_y[y][x + 1])
                self._image_draw.line(coords, fill=fill_color)

    def build(self):
        """Create new captcha image."""

        self._image = Image.new('RGB', self._size, (255, 255, 255))
        self._image_draw = ImageDraw.Draw(self._image)
        self.word = [random.choice(self._symbols) for _ in range(4)]

        self._grid_gen()

        self._draw_lines_from_symbols()

        self._pixels = self._image.load()

        self._draw_grid()
    
    def ret_name(self):
        """return name of the CAPTCHA"""
        return self.word

    def show(self):
        """Shows captcha image."""

        self._image.show()

    def save(self, filename):
        """Saves captcha image to file."""

        self._image.save(filename)

    def base64(self, image_format='JPEG'):
        """Returns a base64 encoded picture."""

        ret = io.BytesIO()
        self._image.save(ret, format=image_format)
        ret.seek(0)

        return b64encode(ret.getvalue()).decode()
