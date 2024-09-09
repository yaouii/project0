class item:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
      
    
    inventory = ['']

    def reciveitem(self, name):
        self.inventory.append(name)# ai filled in this
        print("you recived" + self.name)
        

    def checkinventory():
        print(self.inventory)