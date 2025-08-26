import re
import random
from enum import Enum

class GameCommand(Enum):
    MOVE = 1
    ATTACK = 2
    CAST = 3

class GameParser:
    def __init__(self):
        self.commands = {
            r"move (north|south|east|west)": GameCommand.MOVE,
            r"attack (enemy|monster)": GameCommand.ATTACK,
            r"cast (fireball|heal)": GameCommand.CAST
        }

    def parse(self, command):
        for pattern, action in self.commands.items():
            match = re.match(pattern, command, re.IGNORECASE)
            if match:
                return action
        return None

class Game:
    def __init__(self):
        self.parser = GameParser()

    def play(self):
        while True:
            command = input("Enter a command: ")
            action = self.parser.parse(command)
            if action == GameCommand.MOVE:
                print("Moving...")
            elif action == GameCommand.ATTACK:
                print("Attacking...")
            elif action == GameCommand.CAST:
                print("Casting...")
            else:
                print("Invalid command. Try again!")

if __name__ == "__main__":
    game = Game()
    game.play()