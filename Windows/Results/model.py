import json
from pathlib import Path


class Model:
    @staticmethod
    def players_results(match_id=1):
        # return get_players_and_results(match_id)
        return [["Bobbi", "scissors", "dead"],
                ["Toddi", "rock"    , "win" ]]

