class Car:
    def __init__(self, speed: int, model: str):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param speed: Скорость автомобиля
        :param model: Марка автомобиля

        Примеры:
        >>> car = Car(120, "Opel") #Инициализация экземпляра класса
        """

        if not isinstance(speed, int):
            raise TypeError("Скорость автомобиля должна быть типа int")
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной")
        if speed > 280:
            raise ValueError("Так быстро нельзя даже на автобанах...")
        self.speed = speed

        if not isinstance(model, str):
            raise TypeError("Марка автомобиля должна быть строкой")
        self.model = model

    def accelerate(self, raise_speed: int = 0) -> None:
        """
        Функция которая прибавляет скорость автомобиля

        :param raise_speed: На сколько км/ч нужно разогнаться

        :raise ValueError: Если при добавлении скорости скорость превышает 280км/ч

                Примеры:
        >>> car = Car(120, "Opel")
        >>> car.accelerate(100)
        """

        if not isinstance(raise_speed, int):
            raise TypeError("Прибавляемая скорость должна быть типа int")
        if raise_speed < 0:
            raise ValueError("Прибавляемая скорость не может быть отрицательным числом")

        self.speed += raise_speed

    def is_stop(self) -> bool:
        """
        Функция, которая проверяет машина стоит на месте или нет

        :return: стоит ли машина

                Примеры:
        >>> car = Car(0, "Opel")
        >>> car.is_stop()
        True
        """

        if self.speed == 0:
            return True
        else:
            return False

    def emergency_braking(self) -> None:
        """
        Функция, которая полностью тормозит автомобиль в срочном порядке

            Примеры:
        >>> car = Car(120, "Opel")
        >>> car.emergency_braking()
        """

        self.speed = 0


class SocialMedia:
    def __init__(self, name: str, users_count: int):
        """
        Создание и подготовка к работе объекта "Социальная сеть".

        :param name: Название социальной сети
        :param users_count: Количество пользователей

        :raise ValueError: Если количество пользователей меньше 0

        Примеры:
        >>> sm = SocialMedia("Facebook", 2000000000)
        """
        if not isinstance(name, str):
            raise TypeError("Название социальной сети должно быть строкой")
        self.name = name

        if users_count < 0:
            raise ValueError("Количество пользователей должно быть неотрицательным числом")
        if not isinstance(users_count, int):
            raise TypeError("Количество пользователей должно быть типа int")
        self.users_count = users_count

    def add_users(self, new_users: int) -> None:
        """
        Добавление новых пользователей в социальную сеть.

        :param new_users: Количество новых пользователей для добавления

        :raise ValueError: Если количество новых пользователей меньше или равно 0

        Примеры:
        >>> sm = SocialMedia("Facebook", 2000000000)
        >>> sm.add_users(100000)
        """
        if not isinstance(new_users, int):
            raise TypeError("Количество новых пользователей должно быть типа int")
        if new_users <= 0:
            raise ValueError("Количество новых пользователей должно быть положительным числом")

        self.users_count += new_users

    def get_info(self) -> str:
        """
        Получение информации о социальной сети.

        :return: Строка с информацией о социальной сети

        Примеры:
        >>> sm = SocialMedia("Facebook", 2000000000)
        >>> sm.get_info()
        'Социальная сеть Facebook имеет 2000000000 пользователей.'
        """
        return f'Социальная сеть {self.name} имеет {self.users_count} пользователей.'


class Tree:
    def __init__(self, species: str, height: float, age: int):
        """
        Создание и подготовка к работе объекта "Дерево".

        :param species: Вид дерева
        :param height: Высота дерева в метрах
        :param age: Возраст дерева в годах

        :raise ValueError: Если высота меньше или равна 0, или возраст меньше 0

        Примеры:
        >>> tree = Tree("Oak", 5.5, 50)
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой")
        self.species = species

        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть типа int или float")
        if height < 0:
            raise ValueError("Высота дерева должна быть положительным числом")
        self.height = height

        if not isinstance(age, int):
            raise TypeError("Возраст дерева должен быть целым числом")
        if age < 0:
            raise ValueError("Возраст дерева должен быть неотрицательным числом")
        self.age = age

    def grow(self, years: int = 1) -> None:
        """
        Увеличение возраста и высоты дерева.

        :param years: Количество лет для роста (по умолчанию 1)

        :raise ValueError: Если количество лет для роста меньше или равно 0

        Примеры:
        >>> tree = Tree("Oak", 5.5, 50)
        >>> tree.grow(5)
        """
        if not isinstance(years, int):
            raise TypeError("Количество лет должно быть целым числом")
        if years <= 0:
            raise ValueError("Количество лет для роста должно быть положительным числом")

        self.age += years
        self.height += years * 0.5  # Предположим, что дерево растет на 0.5 метра в год

    def get_info(self) -> str:
        """
        Получение информации о дереве.

        :return: Строка с информацией о дереве

        Примеры:
        >>> tree = Tree("Oak", 5.5, 50)
        >>> tree.get_info()
        'Дерево вида Oak высотой 5.5 метров и возрастом 50 лет.'
        """
        return f'Дерево вида {self.species} высотой {self.height} метров и возрастом {self.age} лет.'

