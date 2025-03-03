import doctest
class BankAccount:
    """
    Класс, представляющий банковский счет.

    Атрибуты:
        account_number (str): Номер счета.
        balance (float): Текущий баланс счета.
        interest_rate (float): Процентная ставка по счету.
    """

    def __init__(self, account_number: str, balance: float = 0.0):
        """
        Инициализация объекта банковского счета.

        Аргументы:
            account_number (str): Номер счета.
            balance (float): Начальный баланс счета. По умолчанию 0.0.

        Исключения:
            ValueError: Если начальный баланс.
        """
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным.")

        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Пополнение счета на указанную сумму.

        Аргументы:
            amount (float): Сумма для пополнения.

        Исключения:
            ValueError: Если сумма для пополнения отрицательная.

        Пример:
            >>> account = BankAccount("123456789")
            >>> account.deposit(100.0)
            >>> account.balance
        """
        if amount < 0:
            raise ValueError("Сумма для пополнения не может быть отрицательной.")

        ...

    def withdraw(self, amount: float) -> None:
        """
        Снятие денег со счета.

        Аргументы:
            amount (float): Сумма для снятия.

        Исключения:
            ValueError: Если сумма для снятия отрицательная или превышает баланс.

        Пример:
            >>> account = BankAccount("123456789", 100.0)
            >>> account.withdraw(50.0)
            >>> account.balance
        """
        if amount < 0:
            raise ValueError("Сумма для снятия не может быть отрицательной.")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете.")

        ...

    def transfer(self, target_account: 'BankAccount', amount: float) -> None:
        """
        Перевод денег на другой банковский счет.

        Аргументы:
            target_account (BankAccount): Целевой счет для перевода.
            amount (float): Сумма для перевода.

        Исключения:
            ValueError: Если сумма для перевода отрицательная или превышает баланс.

        Пример:
            >>> account1 = BankAccount("123456789", 100.0)
            >>> account2 = BankAccount("987654321", 50.0)
            >>> account1.transfer(account2, 30.0)
            >>> account1.balance
            >>> account2.balance
        """
        if amount < 0:
            raise ValueError("Сумма для перевода не может быть отрицательной.")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете для перевода.")

        ...

    def get_balance(self) -> float:
        """
        Возвращает текущий баланс счета.

        Возвращает:
            float: Текущий баланс счета.

        Пример:
            >>> account = BankAccount("123456789", 100.0)
            >>> account.get_balance()
        """
        ...

# Пример использования
if __name__ == "__main__":
    doctest.testmod()