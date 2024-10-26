class Room:
    def __init__(self, description):
        self.description = description
        self.connections = {}

    def connect(self, direction, room):
        self.connections[direction] = room

    def get_description(self):
        return self.description

    def get_connections(self):
        return self.connections.keys()


class Game:
    def __init__(self):
        self.current_room = None

    def setup_rooms(self):
        # Create rooms
        living_room = Room("You are in a cozy living room with a warm fireplace.")
        kitchen = Room("You are in a kitchen filled with delicious smells.")
        garden = Room("You are in a beautiful garden with colorful flowers.")

        # Connect rooms
        living_room.connect("north", kitchen)
        living_room.connect("south", garden)
        kitchen.connect("south", living_room)
        garden.connect("north", living_room)

        self.current_room = living_room

    def play(self):
        print("Welcome to the Text-Based Adventure Game!")
        self.setup_rooms()

        while True:
            print("\n" + self.current_room.get_description())
            print("Available directions:", ", ".join(self.current_room.get_connections()))
            command = input("Which direction would you like to go? (type 'exit' to quit): ").lower()

            if command == 'exit':
                print("Thanks for playing!")
                break
            elif command in self.current_room.get_connections():
                self.current_room = self.current_room.connections[command]
            else:
                print("You can't go that way!")

if __name__ == '__main__':
    game = Game()
    game.play()
