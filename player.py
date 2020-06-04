class Player:
    '''attributes, physical_stats, character_class'''
    def __init__(self, name):
        self.name = name
        '''self.attributes = attributes
        self.physical_stats = physical_stats
        self.character_class = character_class'''
        self.level = 0
        self.exp = 0
        self.inventory = []