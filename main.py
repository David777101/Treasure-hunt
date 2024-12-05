class Player:
    def __init__(self, name):
        self.name = name

    def move(self, place):
        return self.name + " has moved to " + place

    def pick_up(self, object1):
        return self.name + " has picked up " + object1


class Map:
    def __init__(self, name_of_place):
        self.name_of_place = name_of_place

class Item:
    def __init__(self, name_of_item):
        self.name_of_item = name_of_item

class NPC(Player):
    def __init__(self, name):
    


