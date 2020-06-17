#!/usr/bin/env python

from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="grid_captcha",
    version='1.0.0',
    description="Python Grid Captcha Generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrgyber/grid_captcha",
    license="MIT",
    author="Nikita Kudryavtsev",
    author_email="mrgyber@mail.ru",
    keywords=["grid", "captcha", "generator"],
    packages=['grid_captcha'],
    package_data={'grid_captcha': ['fonts/*']},
    data_files=[('', ['README.md', 'LICENSE'])],
    install_requires=['numpy', 'Pillow', 'scipy'],
    zip_safe=False,
)
