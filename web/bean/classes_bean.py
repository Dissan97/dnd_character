from model.spell import Spell


class ClassTypeBean:

    def __init__(self):
        self.metadata = {}

    def add_features(self, class_type: str, spells: list[Spell]) -> None:
        self.metadata["class"] = class_type
        self.metadata['spells'] = spells
        return None
