import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk
import random
import sys
import glob
from itertools import combinations


def extract_characters(image_file):
    image = cv2.imread(image_file)
    
    upper = np.array([255,255,255],dtype=np.uint8)
    lower = np.array([200,200,200],dtype=np.uint8)

    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)

    output_g = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    
    ret,thresh = cv2.threshold(output_g,127,255,0)
    im2,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    colors = [(0,255,0),(255,0,0),(0,0,255)]
    coordinates=[]
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        coordinates.append((x,y,w,h))
    coordinates.sort(key=lambda x:x[0])
    print(coordinates)
    c_copy = coordinates[:]

    comb = combinations(list(range(len(coordinates))),2)
    for com in comb:
        curr = c_copy[com[0]]
        curr2 = c_copy[com[1]]
        if curr not in coordinates or curr2 not in coordinates:
            continue
        print("Comparing: "+str(curr) + " with "+str(curr2))
        if (curr2[0] >= curr[0] and curr2[1] >= curr[1] and curr2[0]+curr2[2] <= curr[0]+curr[2] and curr2[1]+curr2[3] <= curr[1] + curr[3]):
                print("Removing 1:" + str(curr2))
                coordinates.remove(curr2)
        elif (curr2[0] >= curr[0] and curr2[0]+curr2[2] <= curr[0]+curr[2] and curr2[1] <= curr[1] and curr2[1]+curr2[3] <= curr[1] + curr[3]):
                print("Removing 2:" + str(curr2))
                ind = coordinates.index(curr)
                coordinates[ind] = (curr[0],curr2[1],curr[2],(curr[1]+curr[3])-curr2[1])
                coordinates.remove(curr2)
                


    digits = []
    for coord in coordinates:
        crop_img = output[coord[1]:coord[1]+coord[3], coord[0]:coord[0]+coord[2]]
        digits.append(crop_img)
    return digits
            
def ask_user(image_file):
    window = tk.Tk()
    img = ImageTk.PhotoImage(Image.open(image_file))
    panel = tk.Label(window, image = img)
    panel.pack(side = "top", fill = "both", expand = "yes")
    L1 = tk.Label(window, text="Enter captcha")
    L1.pack( side = tk.LEFT)
    captcha = tk.StringVar()
    def get_captcha():
        print(captcha.get())
        window.destroy()
    
    B = tk.Button(window, text ="Enter", command = get_captcha)
    B.pack(side = tk.RIGHT)
    E1 = tk.Entry(window, bd =5, textvariable = captcha)
    E1.pack(side = tk.RIGHT)
    
    window.mainloop()
    digits = extract_characters(image_file)
    if len(digits) != 6:
        print("Number of recognized charcter in "+image_file+" is not 6. Skipped")
        return
    captcha = captcha.get()
    print(len(captcha))
    for index, digit in enumerate(digits):
        recognized = captcha[index]
        samples = glob.glob("dataset/"+recognized+"_*")
        samples.sort()
        number = 1
        if len(samples) > 0:
            number = int(samples[-1].split('_')[-1].split('.')[0]) +1
        cv2.imwrite("dataset/"+recognized+"_"+str(number)+".jpg", digit)
    


files = glob.glob("*.jpeg")
files.sort()
for f in files[11:]:
    ask_user(f)
