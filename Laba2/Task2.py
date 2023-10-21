salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
required_money_capital = 0  # Подушка безопасности, чтобы протянуть 10 месяцев без долгов
for month in range(1, months + 1):
    required_money_capital += spend
    if required_money_capital > 0:
        required_money_capital -= salary
    spend += spend * increase

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(required_money_capital, 2))
