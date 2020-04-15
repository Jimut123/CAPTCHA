#!/usr/bin/env python3
# -*- coding: utf-8 -*-

####################################################################################################

from img_captcha_gen import CaptchaGenerator
from os import path, makedirs

####################################################################################################

# Path to generate Captchas
GEN_CAPTCHAS_FOLDER = "./captchas"

# Captcha image size number (2 -> 640x360)
CAPCTHA_SIZE_NUM = 2

####################################################################################################

# Main Function #

def main():
    '''Main Function'''
    # Create Captcha Generator object of specified size
    CaptchaGen = CaptchaGenerator(CAPCTHA_SIZE_NUM)
    # If it doesn't exists, create captchas folder to store generated captchas
    if not path.exists(GEN_CAPTCHAS_FOLDER):
        makedirs(GEN_CAPTCHAS_FOLDER)
    # Generate 20 captchas
    for i in range(0, 1000000):
        # Use one of the following 9 captcha generation options
        #captcha = CaptchaGen.gen_captcha_image()
        #captcha = CaptchaGen.gen_captcha_image(multicolor=False, margin=False)
        #captcha = CaptchaGen.gen_captcha_image(multicolor=True, margin=False)
        #captcha = CaptchaGen.gen_captcha_image(multicolor=True, margin=True)
        #captcha = CaptchaGen.gen_captcha_image(difficult_level=3)
        captcha = CaptchaGen.gen_captcha_image(difficult_level=4)
        #captcha = CaptchaGen.gen_captcha_image(chars_mode="hex")
        #captcha = CaptchaGen.gen_captcha_image(chars_mode="ascii")
        #captcha = CaptchaGen.gen_captcha_image(difficult_level=5, multicolor=True, chars_mode="ascii")
        image = captcha["image"]
        characters = captcha["characters"]
        if int(i+1)%1000 == 0:
            print("Generated captcha {}: {}".format(str(i+1), characters))
        label = characters+"_"+str(i+1)
        image.save("{}/{}.png".format(GEN_CAPTCHAS_FOLDER, label), "png")
    print("Process completed. Check captchas images at \"{}\" folder.".format(GEN_CAPTCHAS_FOLDER))


if __name__ == '__main__':
    main()
