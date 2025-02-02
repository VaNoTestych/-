


class Car:
    """
    Создание и подготовка к работе объекта "Автомобиль". Базовый класс для всех автомобилей.

    Атрибуты:
    :param weight: Конструкционная масса автомобиля в кг
                   (должен быть непубличным, чтобы предотвратить случайное изменение
                   (т.к. по логике конструкционная масса не должна меняться))
    :param brand: Марка автомобиля(тоже должен быть непубличным, т.к. марка автомобиля не может меняться)
    :param color: Цвет автомобиля(Должен быть непубличным,
                  чтобы предотвратить незапланированное/случайное изменение)

    Пример:
    >>> car = Car(1500, "Opel", "Black")
    """

    def __init__(self, weight: int, brand: str, color: str):
        if not isinstance(weight, int):
            raise TypeError("Конструкционная масса должна быть целым числом.")
        if weight <= 500:
            raise ValueError("Таких легких автомобилей не бывает")
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть непустой строкой.")
        if not isinstance(color, str):
            raise TypeError("Цвет автомобиля должен быть непустой строкой.")

        self._weight = weight
        self._brand = brand
        self._color = color

    # Т.к. это базовые геттеры и сеттеры их можно будет унаследовать
    @property
    def weight(self) -> int:
        """Получить конструкционную массу автомобиля"""
        return self._weight

    @property
    def brand(self) -> str:
        """Получить марку автомобиля"""
        return self._brand

    @property
    def color(self) -> str:
        """Получить цвет автомобиля"""
        return self._color

    @color.setter
    def color(self, new_color: str) -> None:
        if not isinstance(new_color, str):
            raise TypeError("Цвет автомобиля должен быть в формате строки")
        self._color = new_color

    def __str__(self) -> str:
        """Представление автомобиля"""
        return f'Автомобиль марки "{self._brand}"'

    def __repr__(self) -> str:
        """Подробное представление пассажирского автомобиля"""
        return f'{self.__class__.__name__}(weight={self._weight}, brand={self._brand!r}, color={self._color!r})'

    def drive(self) -> str:
        """Метод, который возвращает стандартное сообщение о движении автомобиля."""
        return "Автомобиль едет по дороге"

    def show_documents(self) -> str:
        """Метод для отображения параметров автомобиля."""
        return f'Данный автомобиль имеет следующие параметры: масса "{self._weight}", марка "{self._brand}", цвет "{self._color}"'


# Дочерний класс PassengerCar
class PassengerCar(Car):
    """
    Класс для пассажирских автомобилей, наследующий от Car.

    Атрибуты:
    :param owner: Владелец автомобиля (должен быть непубличным, чтобы избежать некорректного изменения)
    :param number_of_seats: Количество мест в автомобиле (должен быть положительным целым числом)

    Пример:
    >>> passenger_car = PassengerCar(1200, "Toyota", "Blue", "Иванов", 5)
    """

    def __init__(self, weight: int, brand: str, color: str, owner: str, number_of_seats: int):
        super().__init__(weight, brand, color)  # По принципу DRY вызываю функцию super()

        if not isinstance(owner, str):
            raise TypeError("Владелец автомобиля должен быть непустой строкой.")
        if not isinstance(number_of_seats, int):
            raise TypeError("Количество мест должно быть целым числом.")
        if number_of_seats <= 0:
            raise ValueError("Количество мест не может быть меньше или равно 0")

        self._owner = owner
        self._number_of_seats = number_of_seats

    @property
    def owner(self) -> str:
        """Получить владельца автомобиля"""
        return self._owner

    @owner.setter
    def owner(self, new_owner: str) -> None:
        if not isinstance(new_owner, str):
            raise TypeError("Владелец автомобиля должен быть непустой строкой.")
        self._owner = new_owner

    @property
    def number_of_seats(self) -> int:
        """Получить количество мест в автомобиле"""
        return self._number_of_seats

    # __str__ я наследую, т.к. логика программы это позволяет

    # перегружаю repr, т.к. для полного представления класса изначального не хватает
    def __repr__(self) -> str:
        """Подробное представление пассажирского автомобиля"""
        return f'{self.__class__.__name__}(weight={self.weight}, brand={self.brand!r}, color={self.color!r}, owner={self._owner!r}, number_of_seats={self.number_of_seats})'

    # Метод drive наследуется, поэтому здесь не упоминается

    # Перегружаю метод show_documents, т.к. до этого автомобиль был в целом "товаром" и мы как бы предъявляли просто документы, а теперь он зарегестрирован, поэтому есть новые параметры
    def show_documents(self) -> str:
        """Метод для отображения параметров пассажирского автомобиля с учетом владельца."""
        return f'Данный автомобиль имеет следующие параметры: масса "{self.weight}", марка "{self.brand}", цвет "{self.color}", владелец "{self._owner}"'


