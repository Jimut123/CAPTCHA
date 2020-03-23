import glob
import os
import cv2
from tqdm import tqdm
from matplotlib import pyplot as plt

#print(os.listdir("JAM")[:10])
png_files = glob.glob('JAM/*.png')
png_files[:10]

for item in tqdm(png_files):
    im_name = str(item.split('.')[0]).split('/')[1]
    im_exten = str(item.split('.')[1])
    #print(im_name,".",im_exten)
    img_file = cv2.imread(item,cv2.IMREAD_UNCHANGED)
    gray = cv2.cvtColor(img_file, cv2.COLOR_BGR2GRAY)
    #plt.imshow(gray,cmap='gray')
    #print(img_file.shape)
    #plt.show()
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    thresh = cv2.convertScaleAbs(thresh)
    #print(thresh.shape)
    #plt.imshow(thresh,cmap='gray')
    #plt.show()
    path_ = str('JAM/captcha_'+im_name+"."+im_exten)
    #print(path_)
    cv2.imwrite(path_,thresh)
    os.remove(item)
    #break

