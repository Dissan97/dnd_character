import json
from typing import List

from bean.character_beans import RaceBean
from bean.player_beans import PlayerBean
from controller.login_controller import Login
from controller.utils import extract_enums_list
from dao.race_loader import extract_races
from dao.spell_loader import load_spells
from model.character import ClassType, Race, CharacterClass, Character, Inventory
from model.spell import Spell


class SpellController:

    def __init__(self):

        self.spell_list: list[Spell] = None
        self.classes_bean = {}
        self.load_classes_bean()
        pass

    def load_spells(self):
        self.spell_list = load_spells()

    def get_character_spells(self, class_type: str, level=20) -> list[Spell]:

        max_level = 9
        if self.spell_list is None:
            self.load_spells()

        spells_ret = []

        # parse spells

        for spell in self.spell_list:
            if (class_type in spell.metadata['available_class']) and (max_level >= spell.metadata['level']):
                spells_ret.append(spell)

        return spells_ret

    @staticmethod
    def level_parser(level: int):
        pass

    def load_classes_bean(self):
        self.load_spells()
        class_types = [element.value for element in ClassType]
        for ct in class_types:
            self.classes_bean['class'] = ct
            self.classes_bean['spells'] = self.get_character_spells(class_type=ct, level=20)
        pass


class PlayerController:
    __PATH = 'resources/database/characters.json'

    @staticmethod
    def load_characters(name) -> list:
        characters = []

        with open(PlayerController.__PATH, 'r') as json_file:
            data = json.load(json_file)

        if name in data.keys():
            characters = list(data[name])

        return characters

    def __init__(self, login_controller: Login):
        self.player = login_controller.player
        self.init_player()
        self.race_bean = RaceBean(races=PlayerController.get_race_specs())
        self.player_bean = PlayerBean(player=self.player)

    def init_player(self):
        characters = PlayerController.load_characters(self.player.name)
        if len(characters) == 0:
            return
        self.player.characters = characters

    def create_character(self, name: str, race_name: str, character_class: str, abilities: dict):

        character_class = CharacterClass(character_class)
        race = self.race_bean.get_race_by_name(race_name=race_name)
        character = Character(
            name=name,
            race=race,
            character_class=character_class,
            inventory=Inventory(),
            strength=abilities['str'],
            dexterity=abilities['dex'],
            constitution=abilities['con'],
            intelligence=abilities['int'],
            wisdom=abilities['wis'],
            charisma=abilities['cha']
        )

        self.player.assign_character(character)

    @staticmethod
    def get_race_specs() -> list[Race]:
        return extract_races()

    @staticmethod
    def get_classes():
        return extract_enums_list(ClassType)

    def get_player_bean(self):
        return self.player_bean
