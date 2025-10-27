class FileSystemComponent:
    def show_details(self):
        pass

class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print(f"File: {self.name}")

class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def show_details(self):
        print(f"Directory: {self.name}")
        for item in self.items:
            item.show_details()

# ساخت فایل‌ها
file1 = File("file1.txt")
file2 = File("file2.txt")
file3 = File("file3.txt")

# ساخت دایرکتوری‌ها
dir1 = Directory("Documents")
dir2 = Directory("Pictures")
rootDir = Directory("Root")

# اضافه کردن فایل‌ها به دایرکتوری‌ها
dir1.add(file1)
dir1.add(file2)
dir2.add(file3)

# اضافه کردن دایرکتوری‌ها به دایرکتوری ریشه
rootDir.add(dir1)
rootDir.add(dir2)

# نمایش جزئیات کل سیستم فایل
rootDir.show_details()