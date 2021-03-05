class Item():
    def __init__(self, item_name):
        self._name = item_name
        self._description = None
        self.room = None
        self.character = None

    @property
    def description(self):
        return self._description 

    @description.setter
    def description(self, item_description):
        self._description = item_description

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, item_name):
        self._name = item_name 

    def rooms(self, item_name, room):
        self.room[item_name] = room
        # print( self.name + " in :" + repr(self.room) )

    def items (self, character):
        self.character = character

    def get_details(self):
        print(self.name)
        print("--------------------")
        print(self.description)
        print(self.name, " in :", self.room)
        
