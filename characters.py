
"""
    Represents a character in the game. Each character has a name, dialogue, an item, and an inventory.
    
    The `Character` class provides methods to interact with the character, including giving them an item and printing their dialogue.
    """
class Character:
    def __init__(self, name, diaogue, item, inventory):
        self.name = name
        self.diaogue = diaogue
        self.item = item # ai filled in this

    inventory = []

    def give(self, item):
        self.inventory.append(item)# ai filled in this

    def interact(self, diaogue):
        print(self.diaogue) # ai filled in this
        continueinteraction = input("Continue talking to them? (y/n)")
        if continueinteraction == "y":
            return True
        else:
            print("you decide to stop talking to them for now")
            return False 
