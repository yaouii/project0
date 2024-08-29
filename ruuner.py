from characters import Character
from items import item
from wordle import playwordle

inventoy = []

print("You find yourself in a field. In front of you is a path. There also seems to be someone waiting behind you.")
choice_1 = input("Continue down the path or turn around? (path or turn)")
if choice_1 == "path":
    Print("you go down the path. You eventually see a village")

elif choice_1 == "turn":
    print("You turn to see what looks like a wandering riddle master.")
    Character = Character("Riddle Master", "'greetings...'")
    print(Character.diaogue + " said the riddle master")
    Choice_b1 = input("'Would you like to solve my riddle? If you do, you shall recieve a special item...' (play/refuse)")
    if Choice_b1 == "play":
        print("'fantastic. We shall begin.'")
        
    elif Choice_b1 == "refuse":
        print("'I understand. It sems you just aren't cool enough. Come back when you find your swag......'")

