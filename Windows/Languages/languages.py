import json

class Languages:
    def __init__(self):
        self.avaliable = [
            "pol",
            "eng",
        ]

    def return_dictionary(self, language: str):
        if language in self.avaliable:
            return json.load("LanguagePack\\{}.json".format(language))
        else:
            return json.load("LanguagePack\\eng.json")

