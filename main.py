class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})" #дочерние классы унаследуют


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом и больше нуля")
        self.pages = pages

    def __str__(self):
        return f"Бумажная книга {self.__name}. Автор {self.__author}. Количество страниц {self.pages}"
        #перегрузила метод __str__, чтобы выводил Бумажная книга


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)

        if not isinstance(duration, float):
            raise TypeError("Продолжительность книги должна быть float")
        if duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом и больше нуля")
        self.duration = duration

    def __str__(self):
        return f"Аудио книга {self.__name}. Автор {self.__author}. Продолжительность {self.duration}"
        #перегрузила метод __str__, чтобы выводил Аудио книга
