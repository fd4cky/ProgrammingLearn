from datetime import datetime
from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass


class Book(Printable):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = int(year)

    @classmethod
    def from_string(cls, data):
        title, author, year = data.split(';')
        return cls(title, author, int(year))

    def print_info(self):
        print(self.info())

    def info(self):
        return f'{self.title} - {self.author}\n{self.year}'
    
    @property
    def age(self):
        return datetime.now().year - self.year
    
    @age.setter
    def age(self, value):
        self.year = datetime.now().year - value
    
    def __str__(self):
        return self.info()
    
    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title
    

class Ebook(Book):
    def __init__(self, title, author, year, format):
        super().__init__(title, author, year)
        self.format = format
    
    def info(self):
        return super().info() + f' - {self.format}'

    
book = Book('name', 'author', 1945)
book2 = Book.from_string('Voina;Ya;5555')
book3 = Ebook('name', 'Cesar', 1200, 'Kniga')


print(book == book3)
print(book.age)
print(book2.age)
print(book3.age)
book.age = 25
print(book)