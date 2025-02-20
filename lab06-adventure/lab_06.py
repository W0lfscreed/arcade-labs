#Crear dungeon

class Room:
    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west

def main():

    room_list=[]

    #Corridors

    corridor1= Room("You are on a dimly lit corridor.", "North", None, None, "West")
    room_list.append(corridor1)

    corridor2 = Room("A long, narrow hallway.", "North", "South", "East", "West")
    room_list.append(corridor2)

    corridor3= Room("A cold, stone passage.", None, "South", "East", None)
    room_list.append(corridor3)

    #Rooms

    room1 = Room("A small room with old furniture.", "North", None, "East", None)
    room_list.append(room1)

    room2 = Room("A dusty chamber.", None, "South", "East", None)
    room_list.append(room2)

    room3 = Room("A mysterious library.", "North", None, None, "West")
    room_list.append(room3)

    room4 = Room("A torch-lit chamber.", None, "South", None, "West")
    room_list.append(room4)

    current_room = room_list[0]

    print(current_room.description)

    done = False
    while not done:
        done=True

    print()

    direction = str(input("Which direction would you like to go? "))

    if  direction == "North" or "n" or "N" or "NorRth":
        direction= "North"
        next_room = room_list[current_room].north

    elif direction == "South" or "s" or "S" or "Soutrth":
        direction= "South"
        next_room = room_list[current_room].south

    elif direction == "East" or "e" or "E" or "East":
        direction= "East"
        next_room = room_list[current_room].east

    elif direction == "West" or "w" or "W" or "West":
        direction= "West"
        next_room = room_list[current_room].west

    else:
        print("You can’t go that way.")
        next_room = room_list[current_room]



main()

