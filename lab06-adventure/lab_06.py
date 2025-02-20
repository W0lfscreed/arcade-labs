#Crear dungeon

class Room:
    def __init__(self, description, north, south, east, west):
        self.description = ""
        self.north = 0
        self.south = 0
        self.east = 0
        self.west = 0

def main():

    room_list=[]

    #Corridors

    corridor1= Room("Room", "North", None, None, "West")
    room_list.append(corridor1)

    corridor2 = Room("Room", "North", "South", "East", "West")
    room_list.append(corridor2)

    corridor3= Room("Room", None, "South", "East", None)
    room_list.append(corridor3)

    #Rooms

    room1 = Room("Room", "North", None, "East", None)
    room_list.append(room1)

    room2 = Room("Room", None, "South", "East", None)
    room_list.append(room2)

    room3 = Room("Room", "North", None, None, "West")
    room_list.append(room3)

    room4 = Room("Room", None, "South", None, "West")
    room_list.append(room4)

    current_room = 0
    print(room_list)


main()
