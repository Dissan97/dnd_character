import model.character as car


class Player:
    def __init__(self, name, characters: list[car.Character] = None):
        self.name = name
        self.characters = characters

    def assign_character(self, character):
        self.characters.append(character)

    def display_player_info(self):
        print(f"Player: {self.name}")
        if self.character:
            print("Character Information:")
            self.character.display_character_info()
        else:
            print("No character assigned yet.")

    def __str__(self):
        msg = self.name

        if self.character is not None:
            msg = msg + f" {str(self.character)}"

        return msg
