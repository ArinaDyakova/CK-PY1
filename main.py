import doctest

class Bouquet:
    def __init__(self, bouquet_count: int, amount: int):
        """
        Создание и подготовка к работе объекта "Букет"

        :param bouquet_count: Букет состоит из 101 розы максимум>
        :param amount: Количество цветов в букете

        Примеры:
        >>> bouquet = Bouquet(101,1) # инициализация экземпляра класса
        """
        if not isinstance(bouquet_count, int):
            raise TypeError("Количество цветов букета должно быть типа int")
        if bouquet_count <= 0:
            raise ValueError("Вес букета должен быть положительным числом и больше нуля")
        self.bouquet_count = bouquet_count

        if not isinstance(amount, int):
            raise TypeError("Количество цветов должно быть int")
        if amount < 0:
            raise ValueError("Количество цветов в букете не может быть отрицательным")
        if amount % 2 == 0:
            raise ValueError("Ваша девушка не оценит такой подарок")
        self.amount = amount

    def add_flower_to_bouquet(self, flower: int) -> None:
        """
        Добавление цветка в букет.
        :param flower: Количество добавляемых цветов

        :raise ValueError: Если количество добавляемых цветов меньше 101, то вызываем ошибку

        Примеры:
        >>> bouquet = Bouquet(101,0)
        >>> bouquet.add_flower_to_bouquet(101)
        """
        if not isinstance(flower, int):
            raise TypeError("Количество добавляемых цветов должно быть int")
        if flower < 0:
                raise ValueError("Количество добавляемых цветов в букете не может быть отрицательным")
        if flower < 100:
            raise ValueError("Количество добавляемых цветов должны быть не меньше 101")

    def remove_flower_from_bouquet(self, estimate_flower: int) -> None:
        """
        Извлечение цветка из букета.

        :param estimate_flower: Количество извлекаемых из букета цветов
        :raise ValueError: Если количество извлекаемых цветов превышает количество цветов в букете,
        то возвращается ошибка.

        :return: Количество реально извелечнных цветов

        Примеры:
        >>> bouquet = Bouquet(101,101)
        >>> bouquet.remove_flower_from_bouquet(1)
        """

        if not isinstance(estimate_flower, int):
            raise TypeError("Количество извлекаемых цветов должно быть int")
        if estimate_flower < 0:
            raise ValueError("Количество извлекаемых цветов в букете не может быть отрицательным")
        if estimate_flower > 101:
            raise ValueError("Количество извлекаемых цветов должны быть не больше 101")
        ...



class Rectangle:
    def __init__(self, length: int, width: int):
        """
        Создание и подготовка к работе объекта "Прямоугольник"

        :param length: Длина прямоугольника
        :param width: Ширина прямоугольника

        Примеры:
        >>> form_rec = Rectangle(5,4) # инициализация экземпляра класса
        """
        if not isinstance(length, int):
            raise TypeError("Длина прямоугольника должена быть типа int")
        if length <= 0:
            raise ValueError("Длина прямоугольника должна быть положительным числом и больше нуля")
        self.length = length

        if not isinstance(width, int):
            raise TypeError("Ширина прямоугольника должена быть типа int")
        if width <= 0:
            raise ValueError("Ширина прямоугольника должна быть положительным числом и больше нуля")
        self.width = width

    def area(self):
        """
        Функция поиска площади прямоугольника.

        :return: Площадь прямоугольника

        >>> form_rec = Rectangle(5,4)
        >>> form_rec.area()
        20
        """
        return self.length * self.width

    def perimetr(self):
        """
        Функция поиска периметра прямоугольника.

        :return: Периметр прямоугольника

        >>> form_rec = Rectangle(5,4)
        >>> form_rec.perimetr()
        18
        """
        return 2 * (self.length + self.width)


class Santa_claus_bag:
    def __init__(self, capacity_present: int, occupied_present: int):
        """
        Создание и подготовка к работе объекта "Мешок Деда Мороза"

        :param capacity_present: Вместительность мешка с подарками
        :param occupied_present: Количество подарков в мешке

        Примеры:
        >>> bag = Santa_claus_bag(200,0) # инициализация экземпляра класса
        """
        if not isinstance(capacity_present, int):
            raise TypeError("Вместимость мешка должна быть типа int")
        if capacity_present <= 0:
            raise ValueError("Вместимость мешка должна быть положительным числом и больше нуля")
        self.capacity_present = capacity_present

        if not isinstance(occupied_present, int):
            raise TypeError("Количество подарков должно быть int")
        if occupied_present <= 0:
            raise ValueError("Количество подарков должна быть положительным числом и больше нуля")
        self.occupied_present = occupied_present

    def add_present_to_bag(self, present: int) -> None:
        """
        Добавление подарка в мешок.
        :param present: Количество добавляемых подарков

        :raise ValueError: Если количество добавляемых подарков больше вместимости мешка,
        то вызываем ошибку

        Примеры:
        >>> bag = Santa_claus_bag(200,0)
        >>> bag.add_present_to_bag(120)
        """
        if not isinstance(present, int):
            raise TypeError("Количество добавляемых подарков должно быть int")
        if present < 0:
                raise ValueError("Количество добавляемых подакров не может быть отрицательным числом")
        if present > 200:
            raise ValueError("Количество добавляемых подакров не должно превышать вместимость мешка")

    def remove_present_from_bag(self, estimate_present: int) -> None:
        """
        Извлечение подакров из мешка.

        :param estimate_present: Количество извлекаемых подакров мз мешка
        :raise ValueError: Если количество извлекаемых подарков превышает квместимость мешка,
        то возвращается ошибка.

        :return: Количество реально извелечнных подарков

        Примеры:
        >>> bag = Santa_claus_bag(200,200)
        >>> bag.remove_present_from_bag(100)
        """

        if not isinstance(estimate_present, int):
            raise TypeError("Количество извлеченных подарков должно быть int")
        if estimate_present < 0:
            raise ValueError("Количество извлекаемых подарков не может быть отрицательным")
        if estimate_present > 200:
            raise ValueError("Количество извлекаемых подарков не может быть больше вместимости мешка")

if __name__ == "__main__":
    doctest.testmod() #тестирование примеров, которые находятся в документе
    pass
