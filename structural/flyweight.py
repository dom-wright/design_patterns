'''
Flyweight

A form of caching. A class may produce a large number of objects, with many potentially sharing the exact same values (intrinsic traits). It is not efficient to have so many duplicate objects all stored in memory. The flyweight pattern solves this by creating a separate flyweight factory class, which maintains a dictionary of all the existing instances. The application will use the factory to either retrieve the instance from its cache, or create a new one.

Example:
The example below shows a class for a text editor character. Each character has a font, size and colour (intrinsic traits). The flyweight factory assumes responsibility for creating and managing the instances. Once the given instance is created or retrieved from the flyweights dictionary, the user can provide the extrinsic traits i.e. character literal for the given task.
'''


class CharacterFlyweight:
    def __init__(self, font, size, colour):
        self.font = font
        self.size = size
        self.colour = colour

    def render(self, character):
        print(
            f"Character: {character}, Font: {self.font}, Size: {self.size}, colour: {self.colour}")


class CharacterFlyweightFactory:
    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, font, size, colour):
        key = (font, size, colour)
        if key not in self.flyweights:
            self.flyweights[key] = CharacterFlyweight(font, size, colour)
        return self.flyweights[key]


class Editor:
    def __init__(self):
        self.content = []

    def add_character(self, character):
        self.content.append(character)


class Editor:
    def __init__(self):
        self.content = []

    def add_character(self, character):
        self.content.append(character)


factory = CharacterFlyweightFactory()

# Character doesn't exist, so created.
character1 = factory.get_flyweight("Arial", 12, "Black")
character1.render("A")

# Character doesn't exist, so created.
character2 = factory.get_flyweight("Times New Roman", 14, "Red")
character2.render("C")

# Character already exists and is retrieved from dictionary.
character3 = factory.get_flyweight("Arial", 12, "Black")
character3.render("B")

print(character1 is character3)


editor = Editor()

editor.add_character(character1.render("H"))
editor.add_character(character1.render("E"))
editor.add_character(character1.render("L"))
editor.add_character(character2.render("L"))
editor.add_character(character2.render("O"))

# Obviously "Character: A, Font: Arial, Size: 12, colour: Black" isn't greatly useful. The output instead might be codes for each letter that tell the programme the letter and how to present it.
