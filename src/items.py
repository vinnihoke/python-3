
class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __str__(self):
        return f"Item name: {self.name}, item desc: {self.desc}"
