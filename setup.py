from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Get words for any langauge.'
LONG_DESCRIPTION = 'A package allows developers to retrieve millions of words for the requested language with just one line of code.'

# Setting up
setup(
    name="WordsPy",
    version=VERSION,
    author="eymenefealtun (Eymen Efe Altun)",
    author_email="<eymenefealtun@hotmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'words', 'extraction', 'word', 'lexicon'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)