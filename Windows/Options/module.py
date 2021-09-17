import json
from pathlib import Path


class Module:
    @staticmethod
    def get_config() -> dict:
        try:
            directory = Path.cwd()
            with open("{}\Windows\config.json".format(directory), "r") as f:
                config = json.load(f)
                return config
        except RuntimeError as err:
            print("Error occured: {}".format(err))

    @staticmethod
    def get_default() -> dict:
        try:
            directory = Path.cwd()
            with open("{}\Windows\config_default.json".format(directory), "r") as f:
                config = json.load(f)
                return config
        except RuntimeError as err:
            print("Error occured: {}".format(err))
        
    @staticmethod
    def overwrite_config(config: dict):
        try:
            directory = Path.cwd()
            with open("{}\Windows\config.json".format(directory), "w") as f:
                json.dump(config, f)
        except RuntimeError as err:
            print("Error occured: {}".format(err))



