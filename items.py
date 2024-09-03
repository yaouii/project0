class item:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        
    inventory = []

    def reciveitem(self, item):
        self.inventory.append(item)
    
    