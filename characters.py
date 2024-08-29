class Character:
    def __init__(self, name, diaogue):
        self.name = name
        self.diaogue = diaogue

    def acceptItem(self, item):
        self.inventory.append(item)