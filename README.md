
  

# WordsPy

  

  

A Python library allows developers to retrieve millions of words for the requested language with just one line of code.

  

  

![LexiExtract](https://raw.githubusercontent.com/eymenefealtun/WordsPy/master/RepoResources/WordsPyIcon.png)

  

  

[![PyPi](https://img.shields.io/pypi/v/wordspy)](https://pypi.org/project/wordspy/) [![Downloads](https://img.shields.io/pypi/dm/wordspy)](https://pypi.org/project/wordspy)

  
## Important Note:
Via this library, you are going to be sending a GET request to the [all-words-in-all-languages](https://github.com/eymenefealtun/all-words-in-all-languages).
  

## Install

WordsPy can be installed using the pip command.

```

pip install WordsPy

```

  

## Example

```python

import WordsPy as Wp

english_language = Wp.English()

english_words = english_language.get_all_words() # return all the available words in language

random_english_words = Wp.get_random_words(turkish_words, 5) # retun 5 random words from the list

```

  

## Available languages

[All words in all languages](https://github.com/eymenefealtun/all-words-in-all-languages)

  
  

## How to contribute?

1. [Fork](https://github.com/eymenefealtun/WordsPy/fork) the repository.

2. Make changes.

3. Submit a pull request.

  

## How to support?

* [Buy me a coffee](https://www.buymeacoffee.com/altuneymenefe)

or

* Bitcoin: 19di2VDYV9cNrvrsqhZJeT8yXqwuRZ5PGx
