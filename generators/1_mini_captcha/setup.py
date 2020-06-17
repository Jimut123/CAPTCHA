import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="miniCaptcha",
    version="1.0.1",
    description="Create Simple Image Captcha For Normal Use",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/imanhpr/miniCaptcha",
    author="Iman Hosseini Pour",
    author_email="imanhpr1999@gmail.com",
    python_requires='>=3.8',
    license="MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=['minicaptcha'],
    include_package_data=True,
    install_requires=["pillow"],
    keywords='captcha text development',

)