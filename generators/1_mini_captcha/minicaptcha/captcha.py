"""Simpel And Fast Image Captcha Genrator.

This Model Help To Users Create Just Simple Image Captcha. 
"""

from PIL import Image, ImageDraw, ImageFont
import random
from string import ascii_letters, digits
import os
from .colors import make_Shade, make_Tint, random_hex_color


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

digitsAndLetters = (digits*4) + ascii_letters

DEFAULTFONT_1 = os.path.join(BASE_DIR,r'fonts\1\PermanentMarker-Regular.ttf')
DEFAULTFONT_2 = os.path.join(BASE_DIR,r'fonts\2\Roboto-Medium.ttf')

OPERATORS = ['+','-']

class ICaptcha:
    """ICaptcha generates a captcha image for you with any length you want.

    ICaptcha Is Able To Generate Random Character-Based Image 
    Or A Captcha Image With the Characters That You Give To It.

    Attributes:
        font: The Font That You Want To Draw With.
        save_path: The Path That You Want Your Image To Be Saved.
    """

    def __init__(self, font= DEFAULTFONT_2, save_path=BASE_DIR):
        self.__font = ImageFont.truetype(font, size=60)
        self.__save_path = save_path
    def __del__(self):
        pass
    @staticmethod
    def generate_character(chr_count=5):
        """Generates Random Character And Digit With The Specific Length That You Give To It.

        Generates Random Character And Digit And Return You A String 
        That You Can Use as A Data, For Comparisons And Writing Images

        Args:
            chr_count: The Number Of Characters That You Want To Generate in a String.
        Returns:
            The String That You Can Use In ICaptcha.write_image()

        """
        return str().join(
            [
                random.choice(
                    (
                        digitsAndLetters
                    )  # its Tuplepy
                ) for i in range(chr_count)
            ]
        )

    @staticmethod
    def math_exp():
        '''simple mathematical expression for using in image captcha

        Returns: Tuple continue expression and answer of it (exp , answer)
        '''
        op = random.choice(OPERATORS)
        if op == '-':
            exp = str(random.randint(1,20)) + op + str(random.randint(1,20))
            while (eval(exp) <= 0):
                exp = str(random.randint(1,20)) + op + str(random.randint(1,20))
            return (exp,eval(exp))
        exp = str(random.randint(1,20)) + op + str(random.randint(1,20)) 
        return (exp, eval(exp))


        return 
    @staticmethod
    def make_line(color, img):
        """Makes Horizontal And Vertical Lines.

        Makes Horizontal And Vertical Lines To Draw
        It In Front Of The Image And Make It More Unreadable.

        Args:
            color: The String That Contains A Hex Color Number For The Color Of Lines.
            img : iThe Image Instance That We Want To Draw Lines In It.
        Returns: 
            ImageDraw.Draw object That Contain Lines For Drawing On The Image.

        """
        draw_line = ImageDraw.Draw(img)

        x = 5
        while x < img.size[0]:
            draw_line.line([(x, 0), (x, 100)], make_Tint(color, 20), 2)
            x += 10
            y = 5
        while y <= 100:
            draw_line.line([(0, y), (img.size[0], y)], make_Tint(color, 20), 2)
            y += 10
        return draw_line

    def __draw_on_image_for_text(self, text):
        """draw all characters in different images

        Draws all the characters in different images 
        and rotates them and calculates the final width of the image.

        Args:
            text: string we want to draw in our image

        Returns:
            A list that contains a tuple
            (image character instance , The width we want our character to draw)
        """
        __num_of_w = 10
        list_of_chr = list()
        for character in text:
            chr_w, chr_h = self.__font.getsize(character)
            __text_image = Image.new('L', (chr_w, chr_h), 0)
            __draw_text_image = ImageDraw.Draw(__text_image)
            __draw_text_image.text((0, 0), character, 255, self.__font)
            __text_image = __text_image.resize((chr_w+20, chr_h+20))

            if character not in OPERATORS :
                __text_image = __text_image.rotate(random.randint(-50, 50), Image.BILINEAR, expand=True)

            __text_image = __text_image.crop(
                __text_image.getbbox())
            list_of_chr.append((__text_image, __num_of_w))

            __num_of_w += random.randint(45, 75)
        return list_of_chr

    def __make_background_image(self, wh):
        """make a background image for your captcha

        this function creates a main background image
        for our captcha with a random hex color.

        Args:
            wh: width of background image

        Return:
            instanse of Image.new() that includes your background with a random hex color
        """
        self.main_color = random_hex_color()  # genrate random color for us
        background_image = Image.new(
            'RGB', (wh+70, 100), self.main_color)

        return background_image

    # Main Contorler

    def write_image(self, text,counter,label,folder, show_test=False, save_img=False):
        """this function make simple image captcha for you

        this funcation make simple captcha image for you that we can use it in your project

        Args:
            text: characters that you want draw it in your captcha image
            show_test: if set it True show captcha image temperray as test resualt
            save_image: if set it to True save The Captcha Image that addres we take it to the class instance
        """
        lst_of_chr = self.__draw_on_image_for_text(text)

        final_wh = lst_of_chr[-1][1]

        pure_background_image = self.__make_background_image(final_wh)
        for item in lst_of_chr:
            pure_background_image.paste(im=make_Shade(self.main_color, 50), box=(
                item[1], random.randint(0, 40)), mask=item[0])

        self.make_line(self.main_color, pure_background_image)
        if show_test:
            pure_background_image.show()
        if save_img:
            pure_background_image.save(f'{folder}/{label}_{counter}.jpg',)
