"""
A script to create the dataset c4l-16x16_550.tar.gz
Author: Jimut
        20-03-2020
# 550 is the minimum number
"""

import glob
import cv2
import os
import string
from tqdm import tqdm
png_files = glob.glob('resized_data/*.png')
index_var = "0123456789"+string.ascii_lowercase+string.ascii_uppercase
index = {}
for char in index_var:
    index[char] = 0

for item in tqdm(png_files):
    img_file = cv2.imread(item,cv2.IMREAD_UNCHANGED)
    get_char = str(item.split('.')[0]).split('/')[1][0]
    #print(get_char)
    if index[get_char]<550:
        index[get_char] += 1
        path_ = str('c4l-16x16_1104/'+get_char+'_{}.png'.format(index[get_char]))
        cv2.imwrite(path_,img_file)


