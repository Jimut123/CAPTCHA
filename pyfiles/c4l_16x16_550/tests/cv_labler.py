import cv2
import numpy as np
import glob
import os
import tkinter as tk
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
files = glob.glob('*.jpeg')


for file_ in files:
    root = tk.Tk()
    image_file = Image.open(file_)
    img = ImageTk.PhotoImage(image_file)
    panel = tk.Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    ent = tk.Entry(root)
    ent.pack()
    #root.mainloop()
    def lol():
        label = ent.get()
        fin_label = "captcha_"+str(label)+".jpeg"
        print(fin_label)
        print(len(str(label)))
        if len(str(label))>1:
            os.remove(file_)
            image_file.save(fin_label)
            plt.imsave(fin_label)
            root.quit()
    if len(ent.get())>0:
        continue
    button = tk.Button(root,text="Next",command=lol)
    button.pack()
    root.mainloop()


