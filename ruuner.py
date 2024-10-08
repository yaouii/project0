"""
Handles the main game loop and interactions for the player in the game world.

The `runner.py` module contains the main game loop and handles player interactions with various characters and items in the game world. It includes functionality for:
- Navigating between a field and a village
- Interacting with an upset character to guess their favorite color
- Purchasing items from a vendor in the village
- Feeding a wombat in the path
- Interacting with a riddle master character
"""
from characters import Character
from items import item
from wordle import playwordle

inventory = []
money = 0

while True:
    print("You find yourself in a field. In front of you is a path. There also seems to be someone waiting behind you.")
    choice_1 = input("Continue down the path or turn around? (path or turn)")

    
    if choice_1 == "path":
        while True:
            print("you go down the path. You eventually see a village") #ai filled in
            talktoguy = input("There are many people standing around. One of them seems in a bad mood. Talk to them?(y/n) or turn back? (turn)")
            if talktoguy == "y":
                colorguy = Character("upset guy", "'sigh...'", "5 dollars", [])
                colorguyinteraction = colorguy.interact("y") 
                if colorguyinteraction == True:
                    print("'you really want to keep talking to me...? thanks..'")
                    print("'my friend forgot my favorite color.... I've told him a million times what it is but he still won't remember it..'")
                    while True:
                        colorguess = input("'its so common that even you could guess it.. hmmm... could you be able to guess it? what do you think it is..?'")
                        if colorguess == "blue":
                            print("'wow! you actually got it! i'm so happy! take this!'") #ai filled in
                            colorguy.give("5 dollars")
                            print("you recived" + colorguy.item )
                            money += 5 #ai filled in
                            print("you currently have: $" + str(money) + " dollars.")
                            break
                        else: 
                            print("'uuughhh.. maybe it's not so common afterall.....'")
                            tryagain = input("they seem sad. Try again? (y/n)")
                            if tryagain == "y":
                                break
                            else:
                                print("you decide to return to the main path")
                            
                        break
                else:
                    print("you decide to leave")
            
            elif talktoguy == "turn":
                break

            while True:
                Choice_a1 = input("you see a stand selling multiple items (look/leave)")
                
                if Choice_a1 == "look":
                    print("There are a few items up for sale")
                    snowgrass = item("snow grass", "a bundle of snow grass.", "$3")
                    paper = item("a piece of paper", "an old looking scrap of paper.", "$1000")
                    print(snowgrass.description, snowgrass.price)
                    print(paper.description, paper.price)
                    

                    while True:   
                        choice_a2 = input("you currently have: $" + str(money) + " dollars. what would you like to buy? (snowgrass/paper/nothing)")
                        if choice_a2 == "snowgrass":
                            if money >= 3:
                                money -= 3
                                snowgrass.reciveitem("snow grass")
                                inventory = snowgrass.inventory
                                print(inventory)
                                print("you leave the stand.")
                                break
                            else:
                                print("you don't have enough money")
                                break #ai filled in

                        elif choice_a2 == "paper":
                            if money >= 1000:
                                money -= 1000
                                paper.reciveitem("paper")
                                inventory = paper.inventory
                                print(inventory)
                                print("you bought the paper. It seems there is something written on the back")
                                print("it says 'magic.' this might be a clue for something")
                                break

                            else:
                                print("you don't have enough money")
                                break
                        else:
                            break
                    if inventory == ['paper']:
                        break

                    print("you conitinue walking and encounter a wombat in the middle of the path. It looks hungry. Maybe you could give it something.")
                    print("inventory: " + str(inventory))
                    if inventory == ['snow grass']:
                        print("you might have something he might like.")
                        feed = input("feed the wombat snow grass? (y/n)")
                        if feed == "y":
                            inventory.remove('snow grass') #ai filled in
                            print("you feed the wombat the snow grass. he looks like he's enjoying it. suddenly he coughs up a green piece of paper. it's a $1000 dollar bill.")
                            money += 1000 #ai filled in
                            print("you now have $" + str(money) + " dollars.")
                            break
                        else:
                            print("you decide not to feed the wombat.") #ai filled in
                            print("you turn back")
                            break
                    else :
                        print("you have nothing to give the wombat. You turn back.") #ai filled in
                elif Choice_a1 == "leave":
                    break


    elif choice_1 == "turn":
        print("You turn to see what looks like a wandering riddle master.") #ai filled in
        riddlemaster = Character("Riddle Master", "'greetings...'", "cake", [])
        riddlemasterinteraction = riddlemaster.interact("y") 

        if riddlemasterinteraction == True:
            Choice_b1 = input("'Would you like to solve my riddle? If you do, you shall recieve a special item...' (play/refuse)")
            if Choice_b1 == "play":
                print("'fantastic. We shall begin.'")
                playerwin = playwordle()
                if playerwin == True:
                    print("'it seems you completed my riddle, congratulations. Please, have this cake'")
                    riddlemaster.give("cake")
                    print("you recived" + riddlemaster.item )
                    print("you've beaten the game. congratulations! thanks for playing")  
                    break
                    
                    
            elif Choice_b1 == "refuse":
                print("'I understand. It sems you just aren't cool enough. Come back when you find your swag......'")
                print("you decide to go back to the field for now")
                break
                

