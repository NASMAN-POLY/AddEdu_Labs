class SocialNetwork:
    """
    Базовый класс для представления социальной сети.
    Атрибуты:
        name (str): Название социальной сети.
        _user_count (int): Количество пользователей (инкапсулировано).
    """
    def __init__(self, name: str, user_count: int):
        """
        Конструктор для SocialNetwork.
        Аргументы:
            name (str): Название социальной сети.
            user_count (int): Количество пользователей.
        """
        self.name = name
        self._user_count = user_count  # Инкапсуляция: защита от прямого изменения количества пользователей.

    def add_user(self) -> None:
        """Увеличивает количество пользователей на 1."""
        self._user_count += 1

    def get_user_count(self) -> int:
        """
        Возвращает количество пользователей.
        Возвращает:
            int: Количество пользователей.
        """
        return self._user_count

    def __str__(self):
        return f"{self.name} (Users: {self._user_count})"

    def __repr__(self):
        return f"SocialNetwork(name={self.name}, user_count={self._user_count})"


class VK(SocialNetwork):
    """
    Дочерний класс для представления социальной сети ВКонтакте.
    Наследует атрибуты и методы от базового класса SocialNetwork.
    Атрибуты:
        name (str): Название социальной сети.
        _user_count (int): Количество пользователей (инкапсулировано).
        founder (str): Основатель социальной сети.
    """
    def __init__(self, name: str, user_count: int, founder: str):
        """
        Конструктор для VK.
        Аргументы:
            name (str): Название социальной сети.
            user_count (int): Количество пользователей.
            founder (str): Основатель социальной сети.
        """
        super().__init__(name, user_count)
        self.founder = founder

    def get_founder(self) -> str:
        """
        Возвращает основателя социальной сети.
        Возвращает:
            str: Имя основателя.
        """
        return self.founder

    def get_user_count(self) -> str:
        """
        Перегрузка метода get_user_count из базового класса.
        Возвращает количество пользователей в формате строки с дополнительной информацией.
        Причина перегрузки: необходимость предоставления более специфичной информации для VK.
        Возвращает:
            str: Строка с количеством пользователей.
        """
        return f"VK has {self._user_count} users."

    def __str__(self):
        return f"{self.name} (Users: {self._user_count}, Founder: {self.founder})"

    def __repr__(self):
        return f"VK(name={self.name}, user_count={self._user_count}, founder={self.founder})"

class Facebook(SocialNetwork):
    """
    Дочерний класс для представления социальной сети Facebook.
    Наследует атрибуты и методы от базового класса SocialNetwork.
    Атрибуты:
        name (str): Название социальной сети.
        _user_count (int): Количество пользователей (инкапсулировано).
        ceo (str): Генеральный директор социальной сети.
    """
    def __init__(self, name: str, user_count: int, ceo: str):
        """
        Конструктор для Facebook.
        Аргументы:
            name (str): Название социальной сети.
            user_count (int): Количество пользователей.
            ceo (str): Генеральный директор социальной сети.
        """
        super().__init__(name, user_count)
        self.ceo = ceo

    def get_ceo(self) -> str:
        """
        Возвращает генерального директора социальной сети.
        Возвращает:
            str: Имя генерального директора.
        """
        return self.ceo

    def get_user_count(self) -> str:
        """
        Перегрузка метода get_user_count из базового класса.
        Возвращает количество пользователей в формате строки с дополнительной информацией.
        Причина перегрузки: необходимость предоставления более специфичной информации для Facebook.
        Возвращает:
            str: Строка с количеством пользователей.
        """
        return f"Facebook has {self._user_count} users."

    def __str__(self):
        return f"{self.name} (Users: {self._user_count}, CEO: {self.ceo})"

    def __repr__(self):
        return f"Facebook(name={self.name}, user_count={self._user_count}, ceo={self.ceo})"