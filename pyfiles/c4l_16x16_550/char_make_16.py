"""
A script to resize all the digits to 16x16 for captcha_4_letter_char.tar.gz, updated version...
For dataset captcha_4_letter, created dataset from this script => resized_data_captcha_4_letter_16x16.tar.gz
Author: Jimut
        22-03-2020
"""

import glob
import cv2
import os
import string
from tqdm import tqdm

png_files = glob.glob('captcha_4_letter/data/*.png')

for item in tqdm(png_files):
    #print(item)
    img_file = cv2.imread(item,cv2.IMREAD_UNCHANGED)
    part_,exten_= item.split('.')
    img_name = part_.split('/')[-1:]
    path_ = str('captcha_4_letter/data/resized_data/'+str(img_name[0])+'.'+str(exten_))
    resized = cv2.resize(img_file, (16,16), interpolation = cv2.INTER_AREA)
    ret, thresh = cv2.threshold(resized, 0, 255, cv2.THRESH_OTSU)
    thresh = cv2.convertScaleAbs(thresh)
    cv2.imwrite(path_,thresh)

