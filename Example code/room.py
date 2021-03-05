class Room():
    number_of_rooms = 0

    def __init__(self, room_name):
        self._name = room_name
        self._description = None
        self.linked_rooms = {}
        self._character = None
        self._item = None
        Room.number_of_rooms = Room.number_of_rooms + 1

    @property
    def item (self):
        return self._item
    @item.setter
    def item(self,new_item):
        self._item=new_item
    
    @property
    def description(self):
        return self._description 

    @description.setter
    def description(self, room_description):
        self._description = room_description

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, room_name):
        self._name = room_name 

    @property
    def character(self):
        return self._character 

    @character.setter
    def character(self, new_character):
        self._character = new_character

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        # print( self.name + " linked rooms :" + repr(self.linked_rooms) )

    def details(self):
        print(self.name)
        print("--------------------")
        print(self._description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room._name + " is " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
