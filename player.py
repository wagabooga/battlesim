class Player:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.level = 0
        self.exp = 0
        self.inventory = []
        class_template = self.create_class_template()
        attributes_dict = class_template[character_class]
        attribute_LUK = attributes_dict["LUK"]
        attribute_DEX = attributes_dict["DEX"]
        attribute_STR = attributes_dict["STR"]
        attribute_INT = attributes_dict["INT"]
        self.attributes = [attribute_LUK, attribute_DEX, attribute_STR, attribute_INT]
        print(self.attributes)

    def create_class_template(self):
        class_template = {
            "mage": {
                "LUK": 2,
                "DEX": 2,
                "STR": 1,
                "INT": 5,
            },
            "thief": {
                "LUK": 3,
                "DEX": 4,
                "STR": 2,
                "INT": 1,
            },
            "warrior": {
                "LUK": 3,
                "DEX": 3,
                "STR": 3,
                "INT": 1,
            },

        }
        return class_template

    def create_physical_stats_template(self):
        create_class_template(self)