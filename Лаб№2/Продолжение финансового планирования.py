salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
max_fin=1000000000
money_capital=max_fin
for i in range(months):
    if i!=0:
        spend=spend*(1+increase)
    money_capital=money_capital+salary-spend
money_capital=int(round(max_fin-money_capital,0))
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
