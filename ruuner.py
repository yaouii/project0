from characters import Character
from items import item

from wordle import playwordle

inventory = []
money = 0

print("You find yourself in a field. In front of you is a path. There also seems to be someone waiting behind you.")
choice_1 = input("Continue down the path or turn around? (path or turn)")
if choice_1 == "path":
    print("you go down the path. You eventually see a village")
    Choice_a1 = input("you see a stand selling multiple items (look/leave)")

    if Choice_a1 == "look":
        print("There are a few items up for sale")
        snowgrass = item("a piece of paper", "a bundle of snow grass.", "$3")
        paper = item("a piece of paper", "an old looking scrap of paper.", "$1000")
        print(snowgrass.description, snowgrass.price)
        print(paper.description, paper.price)

        choice_a2 = input("you currently have: $" + str(money) + " dollars. what would you like to buy? (snowgrass/paper/nothing)")
        if choice_a2 == "snowgrass":
            snowgrass.reciveitem(snowgrass)
            print("you bought the snow grass.")
            print(inventory)
            print("you leave the stand.")

        elif choice_a2 == "paper":
            paper.reciveitem(paper)
            print("you bought the paper.")
            print(inventory)

        else:
            print("you leave the stand.")

    elif Choice_a1 == "leave":
        print("'you conitinue walking and encounter a wombat in the middle of the path'")
        


elif choice_1 == "turn":
    print("You turn to see what looks like a wandering riddle master.")
    Character = Character("Riddle Master", "'greetings...'")
    print(Character.diaogue + " said the riddle master")
    Choice_b1 = input("'Would you like to solve my riddle? If you do, you shall recieve a special item...' (play/refuse)")
    if Choice_b1 == "play":
        print("'fantastic. We shall begin.'")
        
    elif Choice_b1 == "refuse":
        print("'I understand. It sems you just aren't cool enough. Come back when you find your swag......'")
        print("you decide to go back to the field for now")
    

