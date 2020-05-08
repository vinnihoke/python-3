# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, backpack=None):
        self.name = name
        self.current_room = current_room
        self.backpack = [] if backpack == None else backpack

    def __str__(self):
        return f"{self.name} is in {self.current_room}"

    def change_room(self, room):
        self.current_room = room

    def add_backpack(self, item):
        self.backpack.append(item)

    def show_backpack(self):
        if len(self.backpack) == 0:
            print("Backpack empty")
        else:
            for item in self.backpack:
                print(item)

    def drop_item(self, item):
        if len(self.backpack) == 0:
            print("Backpack empty")
        else:
            for i in self.backpack:
                if item == i:
                    dropped = item.name
                    self.backpack.remove(item)
                    return dropped
                else:
                    print("Error has occurred")
