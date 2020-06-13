class Player:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.level = 0
        self.exp = 0
        self.inventory = []

    def create_class_template(self):
        class_template = {
            "Mage": {
                "LUK": 2,
                "DEX": 2,
                "STR": 1,
                "INT": 5,
            },
            "Thief": {
                "LUK": 3,
                "DEX": 4,
                "STR": 2,
                "INT": 1,
            },
            "Warrior": {
                "LUK": 3,
                "DEX": 3,
                "STR": 3,
                "INT": 1,
            },

        }
        return class_template

    def create_physical_stats_template(self):
        create_class_template(self)