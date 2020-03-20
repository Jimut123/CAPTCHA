import sys
import numpy as np
import cv2
import glob
samples =  np.empty((0,200))
characters = []
files = glob.glob('*.jpeg')
for f in files:
    im = cv2.imread(f)
    im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    im = cv2.resize(im,(10,10))
    
    character = f.split('_')[0].split('/')[-1]
    sample = im.reshape((1,100))
    samples = np.append(samples,sample,0)
    characters.append(ord(character))

characters = np.array(characters,np.float32)
characters = characters.reshape((characters.size,1))
print(characters, samples)
np.savetxt('samples.data',samples)
np.savetxt('characters.data', characters)
