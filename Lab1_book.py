import doctest
class Book:
    """
    Класс, представляющий книгу.

    Атрибуты:
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания книги.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Инициализация объекта книги.

        Аргументы:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.

        Исключения:
            ValueError: Если год издания меньше 0 или больше текущего года.
        """
        if year < 0 or year > 2025:
            raise ValueError("Недопустимый год издания.")
        self.title = title
        self.author = author
        self.year = year

    def get_info(self) -> str:
        """
        Возвращает информацию о книге.

        Возвращает:
            str: Строка с информацией о книге.

        Пример:
            >>> book = Book("1984", "George Orwell", 1949)
            >>> book.get_info()
        """
        ...

    def is_antique(self) -> bool:
        """
        Проверяет, является ли книга старинной (старше 100 лет).

        Возвращает:
            bool: True, если книга старинная, иначе False.

        Пример:
            >>> book = Book("1984", "George Orwell", 1949)
            >>> book.is_antique()
        """

        ...

# Пример использования
if __name__ == "__main__":
    doctest.testmod()