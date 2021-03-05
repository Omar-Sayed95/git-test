class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self._conversation = None
        self._char_item = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )
        if self._char_item is not None:
            print ("I have something for you!")

    # Talk to this character
    #modifid from "talk" to "conversation"
    @property
    def conversation(self):
        if self._conversation is not None:
            return("[" + self.name + " says]: " + self._conversation) #modified from print to return
        else:
            return(self.name + " doesn't want to talk to you") #modified from print to return

    # Set what this character will say when talked to
    @conversation.setter
    def conversation(self, conversation):
        self._conversation = conversation

    @property
    def char_item(self):
        return self._char_item
    
    @char_item.setter
    def char_item(self, item):
        self._char_item = item
        
    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character): 
    def __init__(self, char_name, char_description): 
        super().__init__(char_name, char_description)
        self._weakness = None

    @property
    def weakness(self):
        #print (self.weakness)
        return self._weakness

    @weakness.setter
    def weakness(self, enemy_weakness):
        self._weakness = enemy_weakness 

    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False

    def steal (self):
        if fight and char_item is not None:
            return self.char_item
        else:
            print ("You are too weak to steal from" + self.name)

class Friend(Character):
    def __init__(self, char_name, char_description): 
        super().__init__(char_name, char_description)

    def gift(self):
        if char_item is not None:
            return self._char_item
        else:
            print ("I wish I would have somethig for you, my friend")
            
