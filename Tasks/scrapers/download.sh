#!/bin/bash

for i in {1000..10000}
do
	echo "downloading $i no. captcha"
	wget  "https://joaps.iitk.ac.in/genCaptcha.html" -O $i.jpg
done
