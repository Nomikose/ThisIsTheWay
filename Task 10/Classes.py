#The given code declares a Player class, with its attributes and an intro() method.
#Complete the code to take the name and level from user input, create a Player object with the corresponding values
# and call the intro() method of that object.

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")

one = Player("name", "level")
print("Player name:")
one.name = input()
print("Your level:")
one.level = input()
one.intro()