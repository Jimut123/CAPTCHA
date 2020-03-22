#https://cdn3.digialm.com/captchaservice/getImageChallenge?appId=30&imageKey=0.501981575288672&captchaType=alphanumeric&dummy=0.4187081263568555

from bs4 import BeautifulSoup
import glob
from PIL import Image
import wget
import os
from selenium import webdriver
import numpy as np
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


kuber_ = 1

for i in np.arange(0.001,10,0.001):
    url = "https://cdn3.digialm.com/captchaservice/getImageChallenge?appId=30&imageKey={}&captchaType=alphanumeric&dummy={}".format(i,i)
    filename = "captcha_{}.jpeg".format(kuber_)
    kuber_ += 1
    try:
        wget.download(url,filename)
    except Exception as e:
        print(e)
        continue
    #profile = webdriver.FirefoxProfile()
    #profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0")
    #driver = webdriver.Firefox(profile)
    #driver.get(url)
    print(url)
    #driver.close()




