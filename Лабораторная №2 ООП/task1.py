BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book: #Инициализируем класс Book
    def __init__(self, id_: int, name: str, pages: int): #Контсруктор с атрибутами, для каждого указал тип данных, чтобы было легче работать
        self.id_ = id_
        self.name = name #Список атрибутов по заданию. Док тест и проверки решил не делать, т.к. по смыслу задания это тне требуется
        self.pages = pages

    def __str__(self) -> str: #Реализация "волшебного" метода __str__
        return f'Книга "{self.name}"'

    def __repr__(self) -> str: #Реализация метода __repr__ Возвращает строку, показывающую, как может быть инициализирован экземпляр.
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})' #!r нужно, чтобы был валидный код (иначе там бы было слово без кавычек, что не приравнялось бы к строке и вызвало ошибку, т.к. один из атрибутов класса - строка)

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
