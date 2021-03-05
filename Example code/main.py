from room import Room
from item import Item
from character import Enemy, Character, Friend
from rpginfo import RPGInfo

spooky_castle = RPGInfo ("The Spooky Castle")
spooky_castle.welcome()
RPGInfo.info()

kitchen = Room("Kitchen")
kitchen.description="A dank and dirty room buzzing with flies."
dining_hall = Room("Dining Hall")
dining_hall.description="A large room with ornate golden decorations on each wall."
ballroom = Room("Ballroom")
ballroom.description="A vast room with a shiny wooden floor. Huge candlesticks guard the entrance."
print("There are " + str(Room.number_of_rooms) + " rooms to explore.") 

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dave.conversation="Brrlgrh... rgrhl... brains..."
dave.weakness="cheese"
catrina = Character("Catrina","A friendly skeleton.")
catrina.conversation="I got your back, my friend"
dining_hall.character = dave 
kitchen.character=catrina

cheese = Item ("cheese")
cheese.description = "The ideal weapon to fight 'Dave' with."
cheese.room = kitchen
kitchen.item = cheese

key = Item ("key")
key.description = "Use this key to unlock the ballroom's door with."
cheese.character = dave
dave.char_item = key

current_room = kitchen 
character = False
backpack = []

while True: 
    print("\n") 
    current_room.details()

    inhabitant = current_room.character
    enemy = isinstance (inhabitant, Enemy)
    if inhabitant is not None:
        inhabitant.describe()
        character = True

    gift = current_room.item
    if gift is not None:
        print("there is a " , gift.name , " here!")

    command = input("> ")
    if command in ["north", "south", "east", "west"]: 
    	current_room = current_room.move(command) 
    elif command == "talk" and character:
        print (inhabitant.conversation)
    elif command == "fight" and character:
        if enemy:
            print ("You have ", backpack, " in your backpack.")
            fight_with = input("What will you fight with?") 
            #inhabitant.fight(fight_with)
            if fight_with in backpack and inhabitant.fight(fight_with):
                spoil = inhabitant.char_item
                if spoil is not None:
                    backpack.append(spoil.name)
                    print ("You've won a " , spoil.name , " from " , inhabitant.name)
                    print (spoil.description)
                    print ("Backpack: ",backpack)
                current_room.character=None
            else: break
        else:
            print(inhabitant.name + " doesn't want to fight with you")
    elif command == "take" and current_room.item is not None:
        backpack.append(gift.name)
        print ("You've taken the " ,gift.name)
        print (gift.description)
        print ("Backpack: ",backpack)
        current_room.item = None

RPGInfo.author = "Stemate" 
RPGInfo.credits()
