dist = float(input("Результат пробежки первого дня: "))
mission = float(input("Цель: "))
days = 1
while dist < mission:
    dist *= 1.1
    days += 1
print(f'Требуемое количество дней: {days}')