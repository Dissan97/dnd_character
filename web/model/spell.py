from enum import Enum
import random

from model.character import CharacterClass


class SpellType(Enum):
    ACID = "Acid"
    BLUDGEONING = "Bludgeoning"
    COLD = "Cold"
    FIRE = "Fire"
    FORCE = "Force"
    LIGHTNING = "Lightning"
    NECROTIC = "Necrotic"
    PIERCING = "Piercing"
    POISON = "Poison"
    PSYCHIC = "Psychic"
    RADIANT = "Radiant"
    SLASHING = "Slashing"
    THUNDER = "Thunder"


class Spell:
    def __init__(self, name, level, distance, components, duration, description: str, school: str,
                 available_class: list[CharacterClass], is_ritual: str, concentration: str,
                 casting_time):
        self.metadata = {'name': name,
                         'level': int(level),
                         'distance': distance,
                         'components': components,
                         'duration': duration,
                         'description': description,
                         'school': school,
                         'available_class': str(available_class).split(','),
                         'ritual': (is_ritual == 'yes'),
                         'concentration': (concentration == 'yes'),
                         'casting_time': casting_time}

    def __str__(self) -> str:
        return f"name: {self.metadata['name']}"

    def __repr__(self):
        return self.__str__()


class SpellSlot:
    def __init__(self, level, character_class):
        self.max_spell_slots = {}
        self.current_spell_slots = {}

        # Inizializza tutti gli slot degli incantesimi al valore massimo fornito
        for i in range(1, 10):  # Supponendo che gli slot degli incantesimi siano disponibili dal livello 1 al livello 9
            self.max_spell_slots[i] = character_class.get_slots(level)
            self.current_spell_slots[i] = self.max_spell_slots[i]

    def spend_spell_slot(self, level):
        if 1 <= level <= 9 and self.current_spell_slots[level] > 0:
            self.current_spell_slots[level] -= 1
            print(f"Spent a level {level} spell slot.")
        else:
            print(f"Invalid spell slot level or no remaining spell slots at level {level}.")

    def regain_all_spell_slots(self):
        for i in range(1, 10):
            self.current_spell_slots[i] = self.max_spell_slots[i]
        print("All spell slots have been regained.")

    def display_spell_slot_status(self):
        print("Current Spell Slot Status:")
        for i in range(1, 10):
            print(f"Level {i}: {self.current_spell_slots[i]}/{self.max_spell_slots[i]}")
