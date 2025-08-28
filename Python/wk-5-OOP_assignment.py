# ASSIGNMENT 1
class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f'"{self.title}" has been checked out.')
        else:
            print(f'"{self.title}" is already checked out.')

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f'"{self.title}" has been returned.')
        else:
            print(f'"{self.title}" was not checked out.')

    def get_info(self):
        return f'"{self.title}" by {self.author} - {self.pages} pages, Genre: {self.genre}'

# Inheritance
class EBook(Book):
    def __init__(self, title, author, pages, genre, file_size_mb):
        super().__init__(title, author, pages, genre)
        self.file_size_mb = file_size_mb

    # Polymorphism
    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}, File Size: {self.file_size_mb}MB'

# Example of it's usage
book1 = Book("Things Fall Apart", "Chinua Achebe", 328, "postcolonial")
ebook1 = EBook("The River Between", "Ngugi wa Thiong'o", 256, "African Literature", 2)

print(book1.get_info())
book1.check_out()




# ASSIGNMENT 2
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Test
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()