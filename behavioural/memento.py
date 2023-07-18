'''
Memento

Allows you to capture / snapshot and restore the internal state of an object without violating encapsulation. It enables you to save the current state of an object (originator) and restore it later, effectively providing the ability to undo or rollback to a previous state.

Implementation:
- A class to create and save the state
- A caretaker class to hold all versions in order.

Example:
An example could be to add the ability for a text editor to save a version of itself. It could then revert back to this previous version if needed.
'''


class TextEditorMemento:
    def __init__(self, content):
        self.content = content

    def get_content(self):
        return self.content


class TextEditor:
    def __init__(self):
        self.content = ""

    def set_content(self, content):
        self.content = content

    def create_memento(self):
        return TextEditorMemento(self.content)

    def restore_from_memento(self, memento):
        self.content = memento.get_content()


class Caretaker:
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self, index):
        return self.mementos[index]


editor = TextEditor()
caretaker = Caretaker()

editor.set_content("Hello, world!")
caretaker.add_memento(editor.create_memento())

editor.set_content("Python is awesome!")
caretaker.add_memento(editor.create_memento())

editor.set_content("Design patterns in Python")
caretaker.add_memento(editor.create_memento())

# Perform undo
editor.restore_from_memento(caretaker.get_memento(1))
print(editor.content)  # Output: Python is awesome!

# Perform redo
editor.restore_from_memento(caretaker.get_memento(2))
print(editor.content)  # Output: Design patterns in Python
