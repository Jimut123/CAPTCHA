import numpy as np
import cv2
import string
import math
import os
import uuid
from tqdm import tqdm
import argparse
# python captcha.py --width 150 --height 40 --num-characters 4 --path data2 --num-images 1000000
wd, _ = os.path.split(os.path.abspath(__file__))


class Captcha:
    def __init__(self, width=120, height=36, characters_set=None,
                 num_of_characters=4, font_set=None,
                 folder=os.path.join(wd, 'samples'), debug=False):
        """
        :param characters_set: character set, all
        :param font_set: font set
        :param num_of_characters: character count in one pic
        :param folder: the folder to save img
        :param debug: debug mode
        """
        if font_set is None:
            font_set = ['FONT_HERSHEY_COMPLEX', 'FONT_HERSHEY_SIMPLEX',
                        'FONT_ITALIC']
        self.font_set = font_set

        if characters_set is None:
            characters_set = string.ascii_uppercase + string.digits
        if isinstance(characters_set, str):
            self.character = [i for i in characters_set]
        elif isinstance(characters_set, list):
            self.character = characters_set

        self.num_of_characters = num_of_characters
        self.width, self.height = width, height
        self.debug = debug
        self.folder = folder
        if not self.debug and folder:
            if not os.path.exists(self.folder):
                os.makedirs(self.folder)

    def _tilt_img(self, img):
        tmp_img = img.copy()
        tmp_img.fill(255)
        tile_angle = np.random.randint(
            int(100*-math.pi/6), int(100*math.pi/6)
        ) / 100
        height, width, _ = img.shape
        for y in range(width):
            for x in range(height):
                new_y = int(y + (x-height/2)*math.tanh(tile_angle))
                try:
                    tmp_img[x, new_y, :] = img[x, y, :]
                except IndexError:
                    pass
        img[:, :, :] = tmp_img[:, :, :]

    def _shake_img(self, img, outer_top_left, outer_bottom_right,
                   inner_top_left, inner_bottom_right):
        (x1, y1), (x2, y2) = outer_top_left, outer_bottom_right
        (i1, j1), (i2, j2) = inner_top_left, inner_bottom_right
        delta_x = np.random.randint(x1-i1, x2-i2)
        delta_y = np.random.randint(y1-j1, y2-j2)
        area = img[y1:y2, x1:x2, :]
        area_high, area_width, _ = area.shape
        tmp_area = area.copy()
        tmp_area.fill(255)

        for index_y in range(area_high):
            for index_x in range(area_width):
                new_x, new_y = index_x + delta_x, index_y + delta_y
                if new_x < area_width and new_y < area_high:
                    tmp_area[new_y, new_x, :] = area[index_y, index_x, :]

        area[:, :, :] = tmp_area[:, :, :]

    def _distort_img(self, img):
        height, width, _ = img.shape
        tmp_img = img.copy()
        tmp_img.fill(255)

        coef_vertical = np.random.randint(1, 5)
        coef_horizontal = np.random.choice([2, 3, 4]) * math.pi / width
        scale_biase = np.random.randint(0, 360) * math.pi / 180

        def new_coordinate(x, y):
            return int(x+coef_vertical*math.sin(coef_horizontal*y+scale_biase))

        for y in range(width):
            for x in range(height):
                new_x = new_coordinate(x, y)
                try:
                    tmp_img[x, y, :] = img[new_x, y, :]
                except IndexError:
                    pass

        img[:, :, :] = tmp_img[:, :, :]

    def _draw_basic(self, img, text):
        font_face = getattr(cv2, np.random.choice(self.font_set))
        font_scale = 1
        font_thickness = 2
        max_width = max_high = 0
        for i in text:
            (width, height), _ = cv2.getTextSize(
                i, font_face, font_scale, font_thickness)
            max_width, max_high = max(max_width, width), max(max_high, height)

        total_width = max_width * self.num_of_characters
        width_delta = np.random.randint(0, self.width - total_width)
        vertical_range = self.height - max_high
        images = list()
        for index, character in enumerate(text):
            tmp_img = img.copy()
            delta_high = np.random.randint(
                int(2*vertical_range/5), int(3*vertical_range/5)
            )
            bottom_left_coordinate = (
                index*max_width + width_delta,
                self.height - delta_high
            )
            font_color = tuple(int(np.random.choice(range(0, 156)))
                               for _ in range(3))
            cv2.putText(tmp_img, character, bottom_left_coordinate, font_face,
                        font_scale, font_color, font_thickness)
            self._tilt_img(tmp_img)
            images.append(tmp_img)
        height, width, _ = img.shape
        for y in range(width):
            for x in range(height):
                r, g, b = 0, 0, 0
                for tmp_img in images:
                    r += tmp_img[x, y, 0]
                    g += tmp_img[x, y, 1]
                    b += tmp_img[x, y, 2]
                r, g, b = r % 256, g % 256, b % 256
                img[x, y, :] = (r, g, b)

    def _draw_line(self, img):
        left_x = np.random.randint(0, self.width//4)
        left_y = np.random.randint(self.height)
        right_x = np.random.randint(self.width*3//4, self.width)
        right_y = np.random.randint(self.height)
        start, end = (left_x, left_y), (right_x, right_y)
        line_color = tuple(int(np.random.choice(range(0, 156)))
                           for _ in range(3))
        line_thickness = np.random.randint(1, 3)
        cv2.line(img, start, end, line_color, line_thickness)

    def _put_noise(self, img):
        for i in range(600):
            x = np.random.randint(self.width)
            y = np.random.randint(self.height)
            dot_color = tuple(int(np.random.choice(range(0, 156)))
                              for _ in range(3))
            img[y, x, :] = dot_color

    def save_img(self, text):
        img = np.zeros((self.height, self.width, 3), np.uint8)
        img.fill(255)
        self._draw_basic(img, text)
        self._put_noise(img)
        self._distort_img(img)
        self._draw_line(img)

        if self.debug:
            cv2.imshow(text, img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            pass
        else:
            fn = text + ('_'+str(uuid.uuid1())[4: 8])
            cv2.imwrite('{}/{}.jpg'.format(self.folder, fn), img)

    def batch_create_img(self, number=5):
        exits = set()
        while(len(exits)) < number:
            word = ''.join(
                np.random.choice(self.character, self.num_of_characters))
            if word not in exits:
                exits.add(word)
                self.save_img(word)
                if not self.debug:
                    if len(exits) % 1000 == 0:
                        print('{} generated.'.format(len(exits)))
        if not self.debug:
            print('{} captchas saved into {}.'.format(len(exits), self.folder))


if __name__ == '__main__':
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'K', 'M',
               'N', 'P', 'R', 'T', 'U', 'V', 'W', 'X', 'Y']

    parser = argparse.ArgumentParser(description='Generate captchas easily')

    parser.add_argument('--width', help='Width of the generated captcha image',
                        type=int)
    parser.add_argument('--height', help='Height of the generated captcha\
                        image', type=int)
    parser.add_argument('--num-characters', '-nc', help='Number of characters\
                        per image', type=int)
    parser.add_argument('--path', '-p', help='Path to save the generated\
                        captcha images', type=str, default='data/')
    parser.add_argument('--num-images', '-n', help='Number of captcha images\
                        to be generated', type=int, default=5)
    parser.add_argument('--debug', help='Run in debug mode',
                        action='store_true')

    args = parser.parse_args()
    c = Captcha(width=args.width, characters_set=letters, height=args.height,
                folder=args.path, num_of_characters=args.num_characters,
                debug=args.debug)
    c.batch_create_img(args.num_images)
