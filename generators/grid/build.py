from grid_captcha import CaptchaBuilder
from tqdm import tqdm
import os
import shutil
os.system('mkdir data1')
counter = 0
for i in tqdm(range(3000000)):
    builder = CaptchaBuilder()  # Create builder
    builder.build()  # Generate new image
    #print(''.join(builder.ret_name()))
    word = builder.word
    #builder.show()
    builder.save(str(''.join(builder.ret_name())+"_"+str(counter)+".png"))
    image_jpeg = builder.base64()
    image_png = builder.base64(image_format='PNG')
    shutil.move( str(''.join(builder.ret_name())+"_"+str(counter)+".png"), 'data1')
    counter += 1
    
