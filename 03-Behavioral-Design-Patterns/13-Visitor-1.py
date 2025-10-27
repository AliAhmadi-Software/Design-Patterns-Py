class File:
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        visitor.visit_file(self)

    def get_size(self):
        return 10

class Directory:
    def __init__(self, name):
        self.name = name
        self.elements = []

    def add(self, element):
        self.elements.append(element)

    def accept(self, visitor):
        visitor.visit_directory(self)

class FileSystemVisitor:
    def visit_file(self, file):
        raise NotImplementedError

    def visit_directory(self, directory):
        raise NotImplementedError

class SizeVisitor(FileSystemVisitor):
    def __init__(self):
        self.total_size = 0

    def visit_file(self, file):
        self.total_size += file.get_size()
        print(f"File Name: {file.name}, File Size: {file.get_size()}")

    def visit_directory(self, directory):
        print(f"Directory Name: {directory.name}")
        for element in directory.elements:
            element.accept(self)

class PrintVisitor(FileSystemVisitor):
    def visit_file(self, file):
        print(f"File Name: {file.name}")

    def visit_directory(self, directory):
        print(f"Directory Name: {directory.name}")
        for element in directory.elements:
            element.accept(self)

if __name__ == "__main__":

    file1 = File("file1.txt")
    file2 = File("file2.txt")
    dir1 = Directory("dir1")
    dir2 = Directory("dir2")

    dir1.add(file1)
    dir2.add(file2)
    dir2.add(dir1)

    size_visitor = SizeVisitor()

    dir2.accept(size_visitor)
    print(f"Total Size: {size_visitor.total_size}")

    print_visitor = PrintVisitor()
    dir2.accept(print_visitor)
