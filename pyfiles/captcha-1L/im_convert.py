import glob
import cv2
import os
import string
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np
png_files = glob.glob('images/*.png')

from tqdm import tqdm
kernel = np.ones((2,2),np.uint8)
for item in tqdm(png_files):
    img_file = cv2.imread(item, cv2.IMREAD_UNCHANGED)
    get_alpha = cv2.split(img_file)[3]
    erosion = cv2.erode(get_alpha,kernel,iterations = 2)
    cv2.imwrite(item,get_alpha)



