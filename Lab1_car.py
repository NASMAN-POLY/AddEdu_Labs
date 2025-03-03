import doctest

class Car:
    """
    Класс, представляющий автомобиль.

    Атрибуты:
        make (str): Марка автомобиля.
        model (str): Модель автомобиля.
        year (int): Год выпуска автомобиля.
        owners (list): Список всех владельцев автомобиля.
    """

    def __init__(self, make: str, model: str, year: int):
        """
        Инициализация объекта автомобиля.

        Аргументы:
            make (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска автомобиля.

        Исключения:
            ValueError: Если год выпуска меньше 1886 (год создания первого автомобиля) или больше текущего года.
        """
        if year < 1886 or year > 2023:
            raise ValueError("Недопустимый год выпуска.")
        self.make = make
        self.model = model
        self.year = year
        self.owners = []  # Изначально список владельцев пуст

    def get_info(self) -> str:
        """
        Возвращает информацию об автомобиле.

        Возвращает:
            str: Строка с информацией об автомобиле.

        Пример:
            >>> car = Car("Toyota", "Corolla", 2020)
            >>> car.get_info()
        """
        ...
    def is_vintage(self) -> bool:
        """
        Проверяет, является ли автомобиль винтажным (старше 25 лет).

        Возвращает:
            bool: True, если автомобиль винтажный, иначе False.

        Пример:
            >>> car = Car("Lexus", "NX", 2025)
            >>> car.is_vintage()

        """
        ...

    def add_owner(self, owner_name: str) -> None:
        """
        Добавляет нового владельца автомобиля.

        Аргументы:
            owner_name (str): Имя нового владельца.

        Пример:
            >>> car = Car("Toyota", "Corolla", 2020)
            >>> car.add_owner("John Doe")
            >>> car.get_owners()
        """
        ...

    def get_owners(self) -> list:
        """
        Возвращает список всех владельцев автомобиля.

        Возвращает:
            list: Список всех владельцев.

        Пример:
            >>> car = Car("Toyota", "Corolla", 2020)
            >>> car.add_owner("John Doe")
            >>> car.add_owner("Jane Smith")
            >>> car.get_owners()
        """
        ...

# Пример использования
if __name__ == "__main__":
    doctest.testmod()