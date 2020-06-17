'''
Created on Dec 30, 2018
'''


from image import WheezyCaptcha
import fire
import random
import os
import shutil
from tqdm import tqdm

#_characters = 'adefhjkmnprstuvwxyABDEFHJKLMNPRSTUVWXY34578'
_characters = 'ABCDEFGHJKLMNPRSTUVWXY3456789'
#"345689abcdeghjkmnprstuvwxy"


    
def gen(amount,repeat=1,fonts_dir="fonts/",out_dir="data/"):
    files = os.listdir(fonts_dir)
    fonts=[]
    for name in files:
        if ".ttf" in name:
            fonts.append(fonts_dir+name)
    image = WheezyCaptcha(fonts=fonts,
                        font_sizes=[90],
                       squeeze_factor=0.5,
                       border=2
                       
                       )
    # im = image.generate_dbg('3A9B')
    for _ in tqdm(range(amount)):
        sizes = [4, 5]
        chars = random.sample(_characters, random.choice(sizes))
        seed = "".join(chars)
        if len(seed) == 5:
            font_size = 100
        else:
            font_size = 120
        for i in range(repeat):
            im = image.generate_dbg(str(seed), font_size=font_size)
#         im.show()
            im.save(out_dir+seed+"_"+str(_) + ".png", format="png")
#fire.Fire()
gen(1000000)
print("Zipping Wait...")
shutil.make_archive('data', 'zip', 'data')
print("Process done successfully")
    
    
    
    
