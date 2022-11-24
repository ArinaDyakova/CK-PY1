salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев
list_month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #для себя легче первести месяцы в виде списка
for m in list_month: #т.к. количество месяцев определенное - то использую цикл с заданным количеством шагов
    if m == 1: #отдельное условие, так как в 1-ом месяце нет увеличения на 3%
        delta = spend - salary #непогашенная задолженность
        money_capital += delta #накапливаем в подушку
    else: # для оставшихся 9 месяцев
        spend *= 1 + increase
        delta = spend - salary
        money_capital += delta
# TODO Оформить решение

print(round(money_capital))
