from minicaptcha.captcha import ICaptcha
import os
import shutil
from tqdm import tqdm


folder_data_count = 136000      # capacity of one folder
folder_count = 1             # current folder saving status
folder_name = 'data/minicaptcha_{}'.format(folder_count)
os.mkdir(folder_name) 
folder_count += 1
for item in tqdm(range(1,1000000)):
    captcha = ICaptcha(font='Roboto-Medium.ttf',save_path='data')
    random_char = captcha.generate_character(chr_count=4)
    #print(random_char)
    #counter = 1  
    if item % folder_data_count == 0:
        # change folder
        print("Zipping ... Will take some time...  please wait ... ")
        shutil.make_archive(str(folder_name), 'zip', str(folder_name))
        print("Current folder = ",folder_count)
        folder_name = 'data/minicaptcha_{}'.format(folder_count)
        os.mkdir(folder_name) 
        folder_count += 1
    captcha.write_image(random_char,counter=item,label = random_char,folder=folder_name,save_img=True)
print("Zipping ... Will take some time...  please wait ... ")
shutil.make_archive(str(folder_name), 'zip', str(folder_name))
print("Done!")
