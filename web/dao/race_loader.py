import json

from model.character import Race


def extract_races() -> list[Race]:
    path = "resources/database/races.json"
    races: list = []

    with open(path, 'r') as json_file:
        data = json.load(json_file)

    for key in data.keys():
        race = Race(key, data[key])
        races.append(race)

    return races
