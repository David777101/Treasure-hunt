class Player:
    def __init__(self, given_name):
        self.name = given_name
        self.health = 100
        self.inventory_max_space = 50
        self.inventory = []

    def move_to_place(self, new_place):
        return self.name + "has moved to " + new_place

    def pickup(self,new_item):
        return self.name + "has picked up" + new_item
      
    def store(self, new_item):
        if len(self.inventory) < self.inventory_max_space:
            self.inventory += 1
            return self.name + " has stored " + new_item

    def fight(self, new_enemy):
        if self.health > 10:
            return self.name + "is fighting " + new_enemy
        
    def use_item(self):
        return self.name + "has used ..."
    
    def talk(self, new_npc):
        return self.name + "is talking to " + new_npc
    
