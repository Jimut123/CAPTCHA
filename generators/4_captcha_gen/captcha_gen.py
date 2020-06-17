from PIL import ImageFont, Image, ImageDraw
import random
import string
import os
from tqdm import tqdm
import shutil

class Captcha:
    def __init__(self):
        self.key = self.random_key()
        self.font = ImageFont.truetype("Roboto-Medium.ttf", 23)
        self.size = (120, 35)
        self.background = (245, 245, 245)
        self.circle_color = (180, 180, 180)
        self.rotate = [angle for angle in range(-2, 2) if angle != 0]
        self.x_off = 10
        self.y_off = 3
        self.char_color = [(150, 150, 150), (92, 92, 92)]
    def __del__(self):
        pass
    def random_key(self):
        key = ''
        for letter in range(6):
            key += random.choice(string.ascii_lowercase + string.digits)
        return key

    def create_image(self,counter):
        image1 = Image.new("RGB", self.size, self.background)
        draw = ImageDraw.Draw(image1)

        for i in range(4):
            x, y, r = (random.randint(0, 120), random.randint(0, 35), random.randint(3, 20))
            draw.ellipse((x - r, y - r, x + r, y + r), outline=self.circle_color)

        for char in self.key:
            image2 = Image.new("RGBA", self.size)
            draw2 = ImageDraw.Draw(image2)
            draw2.text((self.x_off, self.y_off), text=char, font=self.font, fill=random.choice(self.char_color))
            image2 = image2.rotate(random.choice(self.rotate), expand=1)
            image1.paste(image2, (0, 0), image2)
            self.x_off += 16

        path = "./data/"

        if os.path.exists(path) is False:
            os.mkdir(path)

        image1.save(path + self.key+"_"+str(counter) + ".png")


if __name__ == "__main__":
    [Captcha().create_image(x) for x in tqdm(range(800000))]  # number of captchas to be created
    shutil.make_archive('data', 'zip', 'data')
