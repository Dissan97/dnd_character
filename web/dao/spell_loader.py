from model.spell import Spell
import json


def load_spells() -> list[Spell]:
    path = "resources/database/spells.json"
    spells: list = []

    with open(path, 'r') as json_file:
        data = json.load(json_file)

    for element in data:
        spell = Spell(
            name=element['name'],
            level=element['level'],
            school=element['school'],
            distance=element['range'],
            components=element['components'],
            duration=['duration'],
            description=element['desc'],
            available_class=element['class'],
            is_ritual=element['ritual'],
            concentration=element['concentration'],
            casting_time=element['casting_time']
        )
        spells.append(spell)

    return spells
