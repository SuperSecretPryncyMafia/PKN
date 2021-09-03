import json
from pathlib import Path


class Module:
    @staticmethod
    def get_config() -> dict:
        try:
            directory = Path.cwd()
            print(directory)
            with open("{}\Windows\config.json".format(directory), "r") as f:
                config = json.load(f)
                return config
        except RuntimeError as err:
                print("Error occured: {}".format(err))

    @staticmethod
    def get_default() -> dict:
        try:
            with open("default_config.json", "r") as f:
                config = json.load(f)
                return config
        except RuntimeError as err:
                print("Error occured: {}".format(err))
        
    @staticmethod
    def overwrite_config(config: dict):
        try:
            with open("config.json", "w") as f:
                json.dump(config, f)
        except RuntimeError as err:
                print("Error occured: {}".format(err))



