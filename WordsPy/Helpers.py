import requests


def get_main_url(language):
    return f"https://raw.githubusercontent.com/eymenefealtun/all-words-in-all-languages/main/{language}/{language}.txt"


def extract_array(language_name):
    return requests.get(get_main_url(language_name)).text.split(",")


async def extract_array_async(language_name):
    print("async is currently not available. use default one!")


