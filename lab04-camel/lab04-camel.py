class Room:
    def __init__(self, description, north=None, south=None, east=None, west=None):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west

def main():
    room_list = []

    # Crear habitaciones y pasillos con referencias a sus conexiones
    corridor1 = Room("A dimly lit corridor.", north=1, west=3)
    room_list.append(corridor1)

    corridor2 = Room("A long, narrow hallway.", north=2, south=0, east=4, west=5)
    room_list.append(corridor2)

    corridor3 = Room("A cold, stone passage.", south=1, east=6)
    room_list.append(corridor3)

    room1 = Room("A small room with old furniture.", north=5, east=0)
    room_list.append(room1)

    room2 = Room("A dusty chamber.", south=6, east=1)
    room_list.append(room2)

    room3 = Room("A mysterious library.", north=4, west=1)
    room_list.append(room3)

    room4 = Room("A torch-lit chamber.", south=5, west=2)
    room_list.append(room4)

    # Establecer la habitación inicial
    current_room = 0

    # Mostrar la habitación actual
    print(f"You are in: {room_list[current_room].description}")

main()