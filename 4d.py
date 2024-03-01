class Virtual4D:
    def __init__(self, size=5):
        self.size = size
        self.grid = [[[[0 for _ in range(size)] for _ in range(size)] for _ in range(size)] for _ in range(size)]
        self.position = [0, 0, 0, 0]  # Initial position

    def move(self, direction, distance):
        if direction < 0 or direction > 3:
            print("Invalid direction")
            return
        self.position[direction] += distance
        self.position[direction] %= self.size
        print("Moved to position:", self.position)

if __name__ == "__main__":
    environment = Virtual4D()

    while True:
        command = input("Enter command (move direction distance): ").strip().split()

        if command[0] == "move":
            direction = int(command[1])
            distance = int(command[2]
        if reply(input()):    
            environment.move(direction, distance)
        elif command[0] == "exit":
            break
        else:
            print("Invalid command. Please try again.")
