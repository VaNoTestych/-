class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Получить название книги (только для чтения)."""
        return self._name

    @property
    def author(self) -> str:
        """Получить автора книги (только для чтения)."""
        return self._author

    def __str__(self) -> str:
        """Строковое представление книги."""
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        """Официальное строковое представление книги."""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс для бумажных книг."""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # Используем свойство для проверки

    @property
    def pages(self) -> int:
        """Получить количество страниц."""
        return self._pages

    @pages.setter
    def pages(self, value: int):
        """Установить количество страниц с проверкой."""
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self._pages = value

    def __str__(self) -> str:
        """Строковое представление бумажной книги."""
        return f"Бумажная книга {self.name}. Автор {self.author}. Страниц: {self.pages}"


class AudioBook(Book):
    """Класс для аудиокниг."""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # Используем свойство для проверки

    @property
    def duration(self) -> float:
        """Получить продолжительность аудиокниги."""
        return self._duration

    @duration.setter
    def duration(self, value: float):
        """Установить продолжительность с проверкой."""
        if not isinstance(value, (float, int)):
            raise TypeError("Продолжительность должна быть числом.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = float(value)

    def __str__(self) -> str:
        """Строковое представление аудиокниги."""
        return f"Аудиокнига {self.name}. Автор {self.author}. Продолжительность: {self.duration} часов"


# Примеры использования
if __name__ == "__main__":
    paper_book = PaperBook("1984", "Джордж Оруэлл", 328)
    audio_book = AudioBook("Дюна", "Фрэнк Герберт", 21.5)

    print(paper_book)  # Бумажная книга 1984. Автор George Orwell. Страниц: 328
    print(repr(paper_book))  # PaperBook(name='1984', author='Джордж Оруэлл')

    print(audio_book)  # Аудиокнига Дюна. Автор Frank Herbert. Продолжительность: 21.5 часов
    print(repr(audio_book))  # AudioBook(name='Дюна', author='Фрэнк Герберт')