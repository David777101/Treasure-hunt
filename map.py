import random

class Map:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = [["[]" for x in range(columns)] for y in range(rows)]

    def chest_location(self, row, column):
        self.grid[row][column] = "X"

    def enemy_location(self, num_of_enemies):
        enemy_locations = 0
        while enemy_locations < num_of_enemies:
            row = random.randint(0,self.rows - 1)
            column = random.randint(0,self.columns - 1)
            if self.grid[row][column] == "[]":
                self.grid[row][column] = "(E)"
                enemy_locations += 1
    
    def npc_location(self, num_of_npcs):
        npc_locations = 0
        while npc_locations < num_of_npcs:
            row = random.randint(0,self.rows - 1)
            column = random.randint(0,self.columns - 1)
            if self.grid[row][column] == "[]":
                self.grid[row][column] = "(^)"
                npc_locations += 1

    def item_location(self, num_of_items):
        item_locations = 0
        while item_locations < num_of_items:
            row = random.randint(0,self.rows - 1)
            column = random.randint(0,self.columns - 1)
            if self.grid[row][column] == "[]":
                self.grid[row][column] = "(*)"
                item_locations += 1


    def display_map(self):
        for row in self.grid:
            print(" ".join(row))







