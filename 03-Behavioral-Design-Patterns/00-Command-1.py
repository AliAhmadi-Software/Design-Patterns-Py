class Command:
    def execute(self):
        pass

    def undo(self):
        pass


class WriteCommand(Command):
    def __init__(self, editor, text):
        self.editor = editor
        self.text = text

    def execute(self):
        self.editor.write(self.text)

    def undo(self):
        self.editor.undo_write()


class TextEditor:
    def __init__(self):
        self.content = ""
        self.history = []

    def write(self, text):
        self.history.append(self.content)
        self.content += text
        print(f"Editor Content: {self.content}")

    def undo_write(self):
        if self.history:
            self.content = self.history.pop()
            print(f"Undo: {self.content}")
        else:
            print("Nothing to undo")


class EditorInvoker:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)

    def undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()
        else:
            print("No commands to undo")


editor = TextEditor()
invoker = EditorInvoker()

write_hello = WriteCommand(editor, "Hello")
write_world = WriteCommand(editor, " World")

invoker.execute_command(write_hello)
invoker.execute_command(write_world)

invoker.undo()
invoker.undo()
invoker.undo()