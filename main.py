class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом и больше нуля")
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, newPages):
        if not isinstance(newPages, int):
            raise TypeError("Количество страниц должно быть int")
        if newPages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом и больше нуля")
        self._pages = newPages

    def __str__(self):
        return f"Бумажная книга {self._name}. Автор {self._author}. Количество страниц {self._pages}"
        #перегрузила метод __str__, чтобы выводил Бумажная книга

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)

        if not isinstance(duration, float):
            raise TypeError("Продолжительность книги должна быть float")
        if duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом и больше нуля")
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, newDuration):
        if not isinstance(newDuration, float):
            raise TypeError("Продолжительность книги должна быть float")
        if newDuration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом и больше нуля")
        self._duration = newDuration

    def __str__(self):
        return f"Аудио книга {self._name}. Автор {self._author}. Продолжительность {self._duration}"
        #перегрузила метод __str__, чтобы выводил Аудио книга

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"