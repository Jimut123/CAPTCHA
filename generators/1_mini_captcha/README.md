# miniCaptcha

miniCaptcha can generate simple captchas with random colors.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ICaptcha.

```bash
$ pip install minicaptcha
$ python generate.py

```

## Usage

You can change default font and save path :

```python
from minicaptcha.captcha import ICaptcha

captcha = ICaptcha(font='font_1.ttf',save_path='test/path/dir')
```
ICaptcha() default font is : Roboto-Medium.ttf

default save path is : current absolute path of icaptcha

### simple generated image Captcha
```python
from minicaptcha.captcha import ICaptcha

captcha = ICaptcha()
random_char = captcha.generate_character(chr_count=6)
captcha.write_image(random_char,show_test=True)
```
Result :

![name_330G2T2z0WP81r6](https://user-images.githubusercontent.com/56130647/80805164-8ccc2600-8bcc-11ea-8de2-2b9e8c002783.jpg)

### simple mathematical expression image captcha
You can use icaptcha for generate mathematical expression
```python
from minicaptcha.captcha import ICaptcha

captcha = ICaptcha()
math_exp = captcha.math_exp() # (str -> '19-11' , int -> 8)
captcha.write_image(math_exp[0],show_test=True)
```
Result: 


![name_9G50p1E9w7jr554](https://user-images.githubusercontent.com/56130647/80805250-c56bff80-8bcc-11ea-8c46-feaaa010d092.jpg)

## Example
```python
from minicaptcha.captcha import ICaptcha

captcha = ICaptcha()
random_char = captcha.generate_character(chr_count=6)
captcha.write_image(random_char,show_test=True)
user_input = input('Enter captcha please : ')
if user_input.lower() == random_char.lower():
    print(True)
else :
    print(False)

```

## Contributing
If you think you can improve these codes please send pull request and help me to improve myself at programing.

## License


```
MIT License

Copyright (c) 2020 Iman Hosseini Pour

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

