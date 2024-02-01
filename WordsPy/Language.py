from abc import ABC


class Language(ABC):

    def get_all_words(self):
        print("get all words")

    async def get_all_words_async(self):
        print("get all words async")
