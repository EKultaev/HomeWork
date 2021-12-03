proceeds = float(input("Введите значение выручки в рублях: "))
costs = float(input("Введите значение издержек в рублях: "))

if proceeds > costs:
    print(f"Фирма работает в прибыль. Прибыль составляет: {proceeds-costs} руб.")
    rent = (proceeds - costs) / proceeds
    print(f"Рентабильность выручки: {rent:.2f}")
    humans = int(input("Введите численность сотрудников фирмы: "))
    perhumans = (proceeds - costs) / humans
    print(f"Прибыль фирмы в расчете на одного сотрудника: {perhumans:.2f} руб.")
elif proceeds < costs:
    print(f"Фирма работает в убыток. Убыток составляет: {proceeds-costs} руб.")
else:
    print(f"Фирма работает без финансового результата")