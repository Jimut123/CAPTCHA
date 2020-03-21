"""
A script to extract all the digits from the captcha, updated version...
Author: Jimut
        20-03-2020
"""


import glob
import cv2
import os
import string
from tqdm import tqdm
png_files = glob.glob('captcha_4_letter/*.png')

index_var = "0123456789"+string.ascii_lowercase+string.ascii_uppercase

# create a dictionary to keep track of the letter
index = {}
for char in index_var:
    index[char]=0

# actual character extraction code

for item in tqdm(png_files):
    item_ = item.split('/')[1]
    item_name = item_.split('.')[0]
    #print(item_name)
    char_ = [ch for ch in item_name]
    img_file = cv2.imread(item)
    gray = cv2.cvtColor(img_file, cv2.COLOR_BGR2GRAY)
    #plt.imshow(gray,cmap='gray')
    #plt.show()
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    thresh = cv2.convertScaleAbs(thresh)
    #plt.imshow(thresh,cmap='gray')
    #plt.show()
    thres = thresh.copy()
    k = 0

    ROI_number = 0
    """
                0 0 0 0 0 0 0 0 
                0 0 0 3 0 4 0 0 
                0 0 1 0 4 3 0 0 
                0 0 2 0 4 4 0 0 
                0 0 1 0 4 0 0 0
                0 0 0 4 3 0 0 0
                0 0 0 0 0 0 0 0
                0 0 0 0 0 0 0 0
                    
                    |\/|
                
                    0 0 0 0 
                    0 3 0 4 
                    1 0 4 3 
                    2 0 4 4 
                    1 0 4 0 
                    0 4 3 0 
                    0 0 0 0 
                    0 0 0 0 
    """
    for y in range(thresh.shape[1]):
        dummy = 0
        for x in range(thresh.shape[0]):
            #print(thresh[x][y],end=" ")
            if thresh[x][y] == 0:
                # if character is found
                dummy = 1
        if dummy ==1:
            if k ==1:
                sart_col = y
            k += 1
        if dummy == 0 and k >2:
            end_col = y
            k1 = 0
            # find contours within that region
            #print("Start = ",sart_col," End = ",end_col)
            extract_im = thresh[:,sart_col-2:end_col+1].copy()
            """
                0 0 0 0 
                0 3 0 4 
                1 0 4 3 
                2 0 4 4 
                1 0 4 0 
                0 4 3 0 
                0 0 0 0 
                0 0 0 0 

                  |\/|
                   
                0 3 0 4 
                1 0 4 3 
                2 0 4 4 
                1 0 4 0 
                0 4 3 0 
            """
            for x1 in range(extract_im.shape[0]):
                dummy1 = 0
                for y1 in range(extract_im.shape[1]):
                    if extract_im[x1][y1] == 0:
                        #if char is found
                        dummy1 = 1
                if dummy1 == 1:
                    if k1 == 1:
                        start_row = x1
                    k1 += 1
                if dummy1 == 0 and k1>2:
                    end_row = x1
                    #print("Start row = ",start_row," End = ",end_row)
                    ROI = extract_im[start_row-2:end_row+1,:].copy()
                    ROI = 255 - ROI #inverse it
                    if ROI_number>=4:
                        continue
                    cv2.imwrite('captcha_4_letter/data/{}-{}.png'.format(char_[ROI_number],index[char_[ROI_number]]), ROI)
                    index[char_[ROI_number]] += 1
                    break
            k=0
            #print("ROI_num = ",ROI_number)
            ROI_number += 1
