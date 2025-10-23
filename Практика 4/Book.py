from datetime import datetime
from abc import ABC, abstractmethod


class Printable(ABC):
    """Абстрактный класс, представляющий объект с возможностью печати информации."""

    @abstractmethod
    def print_info(self):
        """Выводит информацию об объекте."""
        pass


class Book(Printable):
    """Класс, представляющий книгу с названием, автором и годом издания."""

    def __init__(self, title, author, year):
        """Инициализирует объект книги.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.
        """
        self.title = title
        self.author = author
        self.year = int(year)

    @classmethod
    def from_string(cls, data):
        """Создает объект книги из строки с разделителями.

        Args:
            data (str): Строка с данными книги в формате 'название;автор;год'.

        Returns:
            Book: Новый объект книги.
        """
        title, author, year = data.split(';')
        return cls(title, author, int(year))

    def print_info(self):
        """Выводит информацию о книге."""
        print(self.info())

    def info(self):
        """Возвращает строку с информацией о книге.

        Returns:
            str: Информация о книге в формате 'название - автор\nгод'.
        """
        return f'{self.title} - {self.author}\n{self.year}'

    @property
    def age(self):
        """int: Возраст книги, вычисляемый как разница между текущим годом и годом издания."""
        return datetime.now().year - self.year

    @age.setter
    def age(self, value):
        """Устанавливает возраст книги, изменяя год издания.

        Args:
            value (int): Новый возраст книги.
        """
        self.year = datetime.now().year - value

    def __str__(self):
        """Возвращает строковое представление книги.

        Returns:
            str: Информация о книге.
        """
        return self.info()

    def __eq__(self, other):
        """Сравнивает две книги по названию.

        Args:
            other (object): Объект для сравнения.

        Returns:
            bool: True, если другие объект - книга с таким же названием, иначе False.
        """
        return isinstance(other, Book) and self.title == other.title


class Ebook(Book):
    """Класс, представляющий электронную книгу с форматом файла."""

    def __init__(self, title, author, year, format):
        """Инициализирует объект электронной книги.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.
            format (str): Формат электронной книги.
        """
        super().__init__(title, author, year)
        self.format = format

    def info(self):
        """Возвращает строку с информацией о электронной книге.

        Returns:
            str: Информация о книге с указанием формата.
        """
        return super().info() + f' - {self.format}'


book = Book('name', 'author', 1945)
book2 = Book.from_string('Voina;Ya;5555')
book3 = Ebook('name', 'Cesar', 1200, 'Kniga')


print(book == book3)
print(book.age)
print(book2.age)
print(book3.age)
book.age = 25
print(book3)