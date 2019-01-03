from sys import exit

hasCat = False
hasTea = False

def end_game():
    if hasCat == True and hasTea == True:
        print("You've got your tea and tibs has settled on the couch. Good job!")
    elif hasCat == True and hasTea == False:
        print("Tibs has settled on the couch but you're still thirsty. Good job!")
    elif hasCat == False and hasTea == True:
        print("You've got your tea, but you miss your cat. Good job!")
    elif hasCat == False and hasTea == False:
        print("Your exhaustion supercedes your desires. You collapse on the couch in want of tea and longing for your cat. Good job!")
    exit(0)

def bedroom():
    print("The still bedroom is before you. The bed is made and the room is free of clutter.")

    choice = input("> ")
    choice.lower()

    if "living room" in choice or "leave" in choice:
        living_room()
    elif "call" in choice:
        print("There is no response.")
        bedroom()
    elif "look" in choice:
        print("You check everywhere in the room but Tibs is nowhere to be seen.")
        bedroom()
    else:
        bedroom()

def laundry_room():
    print("The dryer is running in the laundry room where you stand. The kitchen is behind you.")

    choice = input("> ")
    choice = choice.lower()

    if "tibs" in choice or "cat" in choice and "search" in choice or "look" in choice:
        global hasCat
        hasCat = True
        print("You find tibs behind the washer and dryer. What was she doing back there?")
        laundry_room()
    elif "kitchen" in choice:
        kitchen()
    else:
        laundry_room()

def kitchen():
    print("You stand in the kitchen. The kettle and tea supplies are on the counter. The laundry room is to your right and the living room is behind you.")

    choice = input("> ")
    choice = choice.lower()

    if "make tea" in choice:
        global hasTea
        hasTea = True
        print("You take a few moments to prepare a hot cup of tea.")
        kitchen()
    elif "laundry room" in choice:
        laundry_room()
    elif "living room" in choice:
        living_room()
    else: 
        kitchen()
    

def living_room():
    description = "You stand in the living room of the apartment after a long day of binning."
    if hasCat == False and hasTea == False:
        description += " You long for a cup of tea and your cat."
    elif hasCat == True and hasTea == False:
        description += "Tibs is on the couch but you still long for a cup of tea."
    elif hasCat == True and hasTea == True:
        description += " You've got your cup of tea and tibs is waiting for you on the couch"
    
    description += " The kitchen is to your right, the couch is to your left and bedroom is in front of you. What will you do?"
    print(description)

    choice = input("> ")
    choice = choice.lower()

    if "kitchen" in choice:
        kitchen()
    elif "bedroom" in choice:
        bedroom()
    elif "call" in choice:
        print("You call for the cat, but there is no response")
        living_room()
    elif "couch" in choice:
        end_game()
    else:
        living_room()

living_room()
