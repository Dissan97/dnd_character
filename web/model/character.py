import random
from enum import Enum

from model.stuff import Item


class ClassType(Enum):
    BARBARIAN = "Barbarian"
    BARD = "Bard"
    CLERIC = "Cleric"
    DRUID = "Druid"
    FIGHTER = "Fighter"
    MONK = "Monk"
    PALADIN = "Paladin"
    RANGER = "Ranger"
    ROGUE = "Rogue"
    SORCERER = "Sorcerer"
    WARLOCK = "Warlock"
    WIZARD = "Wizard"


class CharacterClass:
    def __init__(self, class_type, spell_map, active_spells, spell_slot):
        self.class_type = class_type
        self.spell_map = spell_map
        self.active_spells = active_spells
        self.spell_slot = spell_slot


class Race:
    def __init__(self, name, race_data):
        self.name = name
        self.race_data = race_data


class Inventory:
    def __init__(self):
        self.items: list[Item] = []

    def add_item(self, item: Item):
        self.items.append(item)
        print(f"Added {item.name} to the inventory.")

    def remove_item(self, item):
        for i in self.items:
            if i == item:
                self.items.remove(i)
        print(f"{item} not found in the inventory.")

    def display_inventory(self):
        print("Inventory:")
        if not self.items:
            print("Empty")
        for item in self.items:
            item.display_item_info()
            print("----")


class Character:
    def __init__(self, name: str, race: Race, character_class: CharacterClass, inventory: Inventory, strength=0,
                 dexterity=0, constitution=0, intelligence=0, wisdom=0, charisma=0):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.inventory = inventory
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def display_character_info(self):
        print("Name:", self.name)
        print("Race:", self.race)
        print("Class:", self.character_class)
        print("Attributes:")
        print("  Strength:", self.strength)
        print("  Dexterity:", self.dexterity)
        print("  Constitution:", self.constitution)
        print("  Intelligence:", self.intelligence)
        print("  Wisdom:", self.wisdom)
        print("  Charisma:", self.charisma)

    @staticmethod
    def roll_skill_check():
        return random.randint(1, 20)  # Generates a random number between 1 and 20
