salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
for i in range (months):
    money_capital += spend-salary
    spend += spend*increase


# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
# Но лучше использовать функцию ceil из библиотеки math
if int(money_capital) == money_capital:
    money_capital = int(money_capital)
else:
    money_capital = int(money_capital) + 1
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
