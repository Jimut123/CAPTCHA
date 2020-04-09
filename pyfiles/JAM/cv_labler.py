
from datetime import datetime
import cv2
import numpy as np
import glob
import os
import tkinter as tk
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
#files = glob.glob('JAM/captcha_*.png')
files = glob.glob('*.png')

for file_ in files:
    root = tk.Tk()
    image_file = Image.open(file_)
    print("Opening file => ",file_)
    img = ImageTk.PhotoImage(image_file)
    panel = tk.Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    ent = tk.Entry(root)
    ent.pack()
    captcha_files = glob.glob('JAM/captcha_*.png')
    print("Total labels need to be done => ",len(captcha_files))
    #root.mainloop()
    def lol():
        label = ent.get()
        fin_label = "JAM/"+str(label)+"_{}.png".format(int(datetime.utcnow().timestamp()))
        print("Final label = ",fin_label)
        print("Character label length = ",len(str(label)))
        if len(str(label))==3:
            img_file1 = cv2.imread(file_,cv2.IMREAD_UNCHANGED)
            #print("File name = ",img_file1)
            #print("File's changed name = ",fin_label)
            image_file.save(fin_label)
            plt.imsave(fin_label,image_file)
            #cv2.imwrite(fin_label,img_file1)
            print("Command => ",os.system('ls {}'.format(file_)))
            print("File removed => ",file_)
            os.remove(file_)
            print("Quiting root...")
            root.destroy()
        print("function done...")

    if len(ent.get())==3:
        # if the required file is renamed, then continue
        print("performing the next operation...")
        continue
    button = tk.Button(root,text="Next",command=lol)
    button.pack()
    root.mainloop()
