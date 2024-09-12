
"""
    Represents an item in the game.
    
    The `item` class represents an item that can be collected and stored in the player's inventory. Each item has a name, description, and price.
    
    The `reciveitem` method adds an item to the player's inventory, and prints a message indicating that the item was received.
    
    The `checkinventory` method prints the contents of the player's inventory.
    """
class item:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
      
    
    inventory = [ ]

    def reciveitem(self, name):
        self.inventory.append(name)# ai filled in this
        print("you recived " + self.name)
        

    def checkinventory():
        print(self.inventory) # i don't think i ended up using this 