from map import Map
import random

class Game_play:

    def __init__(self, rows, columns, num_of_enemies, num_of_items, num_of_npcs):
        self.map = Map(rows, columns)
        self.player_location = [0,0]
        self.found_chest = False
        self.map.chest_location(random.randint(0,rows - 1), random.randint(0, columns - 1))
        self.map.enemy_location(num_of_enemies)
        self.map.item_location(num_of_items)
        self.map.npc_location(num_of_npcs)


    def player_movement(self, direction):
        if direction == "w" and self.player_location[0] > 0:
            self.player_location[0] -= 1
        
        elif direction == "s" and self.player_location[0] < self.map.rows - 1:
            self.player_location[0] += 1
        
        elif direction == "a" and self.player_location[1] > 0:
            self.player_location[1] -= 1
        
        elif direction == "d" and self.player_location[1] < self.map.columns - 1:
            self.player_location[1] += 1
        
        else:
            print("It is impossible to go there!")

    def check_player_location(self):
        row, column = self.player_location


        if self.player_location == self.map.chest_location:
            self.found_chest = True
            print("You have found a chest!!!")
        
        elif self.player_location == "(E)":
            print("You have encountered an enemy")
        
        elif self.player_location == self.map.npc_location:
            print("You have encountered an unknown being???")

        elif self.player_location == self.map.item_location:
            print("There is a strange item in front of you")
            
        else:
            print(f"You are at coordinate ({row} , {column})")

    def gameplay(self):
        
        while self.found_chest == False:
            self.map.display_map()
            print(f"\n\nYou're at {self.player_location}")
            movement = input("Where would you like to go to next:\nup(w)\ndown(s)\nleft(a)\nright(d)\n- ").lower()
            self.player_movement(movement)
            self.check_player_location()

g1 = Game_play(5,5,5,5,2)
g1.gameplay()








