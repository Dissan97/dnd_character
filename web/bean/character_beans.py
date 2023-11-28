from model.character import Race


class RaceBean:

    def __init__(self, races: list[Race]):
        self.races = races

    def get_races_names(self):
        list_names = []

        for race in self.races:
            list_names.append(race.name)

        return list_names

    def get_race_by_name(self, race_name) -> Race | None:

        for race in self.races:
            if race.name == race_name:
                return race

        return None
