import json

from model.player import Player

connection_counter = 0

class Login:

    __PATH = 'resources/database/players.json'
    __SUCCESS = 'Success'
    __INVALID_CREDENTIAL = "INVALID_CREDENTIAL"

    def __init__(self):
        self.player: Player = None
        self.error_message = 'Success'
        print({})

    @staticmethod
    def load_players():
        with open(Login.__PATH, 'r') as json_file:
            data = json.load(json_file)

        return data

    def sign_in(self, username: str, password: str) -> int:

        players = Login.load_players()

        if username in players.keys():
            if players[username] == password:
                self.player = Player(name=username)
                self.error_message = Login.__SUCCESS
                return 0

        self.error_message = Login.__INVALID_CREDENTIAL
        return -1

    def sign_up(self, username: str, password: str) -> int:

        players = Login.load_players()

        if username in players.keys():
            self.error_message = Login.__INVALID_CREDENTIAL
            return -1

        metadata = {
            'username': username,
            'password': password
        }

        players.append(metadata)

        with open(Login.__PATH, 'w') as file_json:
            json.dump(players, file_json)
