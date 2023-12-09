import json
import os

from faker import Faker



class InitData:

    def random_word(self):
        fk = Faker(["zh_CN"])
        random_name = fk.word(ext_word_list=None)
        return random_name

