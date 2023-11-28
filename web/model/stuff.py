class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def display_item_info(self):
        print(f"Item: {self.name}")
        print(f"Description: {self.description}")
        print(f"Value: {self.value} gold")


class Weapon(Item):
    def __init__(self, name, description, value, damage, damage_type):
        super().__init__(name, description, value)
        self.damage = damage
        self.damage_type = damage_type

    def display_item_info(self):
        super().display_item_info()
        print(f"Damage: {self.damage}")
        print(f"Damage Type: {self.damage_type}")


class Armor(Item):
    def __init__(self, name, description, value, armor_class):
        super().__init__(name, description, value)
        self.armor_class = armor_class

    def display_item_info(self):
        super().display_item_info()
        print(f"Armor Class: {self.armor_class}")


class Potion(Item):
    def __init__(self, name, description, value, effect):
        super().__init__(name, description, value)
        self.effect = effect

    def display_item_info(self):
        super().display_item_info()
        print(f"Effect: {self.effect}")


class Consumable(Item):
    def __init__(self, name, description, value, effect):
        super().__init__(name, description, value)
        self.effect = effect

    def display_item_info(self):
        super().display_item_info()
        print(f"Effect: {self.effect}")