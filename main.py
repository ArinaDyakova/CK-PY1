class Reinforcement:
    """ Базовый класс арматура. """
    def __init__(self, diameter: int, klas: str):
        if not isinstance(diameter, int):
            raise TypeError("Диаметр арматуры должен быть int")
        if diameter <= 0:
            raise ValueError("Диаметр арматуры должен быть положительным числом и больше нуля")
        self._diameter = diameter
        if not isinstance(klas, str):
            raise TypeError("Класс арматуры должен быть str")
        self._klas = klas
    """ 
    :param diameter: Диаметр арматуры. Непубличные данные, после производства диаметр уже не изменить.
    :param klas: Класс арматуры. Непубличные данные, после производства класс уже не изменить.
    """
    @property
    def diameter(self) -> int:
        return self._diameter

    @property
    def klas(self) -> str:
        return self._klas

    def getRadius(self) -> float:
        return self._diameter / 2
    #метод будет наследоваться в дочерние классы

    def fabrica(self) -> str:
        return "Москва"
    #метод будет перегружаться в дочерних классах. Города производства будут меняться.

    def __str__(self) -> str:
        return f"Диаметр арматуры {self._diameter}. Класс арматуры {self._klas}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(diameter={self._diameter!r}, klas={self._klas!r})"


class WorkingReinforcement(Reinforcement):
    """ Дочерний класс рабочая арматура. """
    def __init__(self, diameter: int, klas: str, force_in_element: float):
        super().__init__(diameter, klas)

        if not isinstance(force_in_element, float):
            raise TypeError("Усилие в элементе должно быть типа float")
        self._force_in_element = force_in_element
    """ 
    :param force_in_element: Усилие в элементе. Рабочая арматура воспринимает усилие, по усилию ее подбирают
    """
    @property
    def force_in_element(self) -> float:
        return self._force_in_element

    @force_in_element.setter
    def force_in_element(self, otherForce) -> None:
        if not isinstance(otherForce, float):
            raise TypeError("Усилие в другом элементе должно быть типа float")
        self._force_in_element = otherForce
    #Усилие может изменяться с течением времени.

    def __str__(self) -> str:
        return f"Диаметр рабочей араматуры {self._diameter}. Класс арматуры {self._klas}. Усилие в элементе {self._force_in_element}."
        #перегрузила метод __str__, чтобы выводил Диаметр рабочей арматуры

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(diameter={self._diameter!r}, klas={self._klas!r}, force_in_element={self._force_in_element!r})."
        #перегрузила метод __repr__, так как в дочернем классе добавилось усилие в элементе

    def fabrica(self) -> str:
        return "Магадан"
    # перегрузка метода. Другой город производства.

class KonstructiveReinforcement(Reinforcement):
    """ Дочерний класс конструктивная арматура. """
    def __init__(self, diameter: int, klas: str, GOST: str):
        super().__init__(diameter, klas)

        if not isinstance(GOST, str):
            raise TypeError("Наименование сортамента должно быть str")
        self._GOST = GOST
    """ 
    :param GOST: Наименование ГОСТ/Сортамента. Конструктивную арматуру назначают согласно нормам
    """
    @property
    def GOST(self) -> str:
        return self._GOST

    @GOST.setter
    def GOST(self, otherGOST) -> None:
        if not isinstance(otherGOST, str):
            raise TypeError("Наименование сортамента должно быть str")
        self._GOST = otherGOST
    #Документация может обновляться.

    def __str__(self) -> str:
        return f"Диаметр конструктивной арматуры {self._diameter}. Класс арматуры {self._klas}. Наименование ГОСТ/Сортамент {self._GOST}"
        #перегрузила метод __str__, чтобы выводил Диаметр конструктивной арматуры

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(diameter={self._diameter!r}, klas={self._klas!r}, GOST={self._GOST!r})"

    def fabrica(self) -> str:
        return "Мурманск"
    # перегрузка метода. Другой город производства.
