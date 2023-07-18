'''
Command pattern

Encapsulates a request as an object, allowing for the logging and queuing of requests, and providing undo capability. It consists of:
- Command: abstract class for commands, setting out interface.
- ConcreteCommand: a concrete command class.
- Receiver: the object that carries out the command, often on itself.
- Invoker: the invoker will line up commands, execute them, and keep a record of completed commands.

Example:
- The below example shows a text editor (receiver), with Command classes that create insert and delete text operations on the receiver.
- All commands are executed through the invoker.
- The invoker keeps a record of all executed commands in order, allowing for undo operations to be completed (as the command themselves hold the information of their actions).
'''

from collections import deque


class TextEditor:

    def __init__(self):
        self.content = ""
        print(f"Editor created.")

    def print_content(self):
        print(self.content)


class Command:
    def execute(self):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError


class InsertText(Command):

    def __init__(self, editor, input_text, start=None):
        self.editor = editor
        self.input_text = str(input_text)
        if start:
            self.start = start
        else:
            self.start = len(self.editor.content)

    def execute(self):
        self.editor.content = self.editor.content[:self.start] + \
            self.input_text + self.editor.content[self.start:]
        self.editor.print_content()

    def undo(self):
        text_length = len(self.input_text)
        self.editor.content = self.editor.content[:self.start] + \
            self.editor.content[self.start + text_length:]
        self.editor.print_content()


class DeleteText(Command):

    def __init__(self, editor, start, length):
        self.editor = editor
        self.start = start
        self.length = length
        self.deleted_text = None

    def execute(self):
        self.deleted_text = self.editor.content[self.start:self.start + self.length]
        self.editor.content = self.editor.content[:self.start] + \
            self.editor.content[self.start + self.length:]
        self.editor.print_content()

    def undo(self):
        self.editor.content = self.editor.content[:self.start] + \
            self.deleted_text + self.editor.content[self.start:]
        self.editor.print_content()


class UpperText(Command):

    def __init__(self, editor, start, length):
        self.editor = editor
        self.start = start
        self.length = length
        self.changed_text = ""

    def execute(self):
        self.changed_text = self.editor.content[self.start:self.start + self.length]
        self.editor.content = self.editor.content[:self.start] + \
            self.changed_text.upper() + \
            self.editor.content[self.start + self.length:]
        self.editor.print_content()

    def undo(self):
        self.editor.content = self.editor.content[:self.start] + \
            self.changed_text + self.editor.content[self.start + self.length:]
        self.editor.print_content()


class Invoker:

    def __init__(self):
        self.undo_queue = deque()
        self.redo_queue = deque()

    def execute_command(self, command):
        command.execute()
        self.undo_queue.appendleft(command)
        self.redo_queue.clear()

    def undo_command(self):
        if self.undo_queue:
            command = self.undo_queue.popleft()
            command.undo()
            self.redo_queue.appendleft(command)
        else:
            print("Nothing to undo")

    def redo_command(self):
        if self.redo_queue:
            command = self.redo_queue.popleft()
            command.execute()
            self.undo_queue.appendleft(command)
        else:
            print("No commands to redo.")


invoker = Invoker()
editor = TextEditor()

insert1 = InsertText(editor, "Here is some good starter text!")
invoker.execute_command(insert1)

insert2 = InsertText(editor, "very ", 13)
invoker.execute_command(insert2)

delete1 = DeleteText(editor, 22, 8)
invoker.execute_command(delete1)

upper1 = UpperText(editor, 13, 4)
invoker.execute_command(upper1)

invoker.undo_command()
invoker.undo_command()
invoker.undo_command()
invoker.undo_command()

invoker.redo_command()
invoker.redo_command()
invoker.redo_command()
invoker.redo_command()
invoker.redo_command()

print()
editor.print_content()
