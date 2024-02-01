from Language import Language
import Helpers as hp


class English(Language):

    def get_all_words(self):
        return hp.extract_array(type(self).__name__)

    async def get_all_words_async(self):
        return hp.extract_array_async(type(self).__name__)
