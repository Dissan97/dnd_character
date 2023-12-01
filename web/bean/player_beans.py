from model.player import Player


class PlayerBean:
    def __init__(self, player: Player):
        self.__player = player

    def get_name(self) -> str:
        return self.__player.name
