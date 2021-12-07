def dif_numbers (a, b):
    if b== 0:
        return "На ноль делить нельзя!!!"
    else:
        return a / b


a = float(input("В веди число 'a': "))
b = float(input("В веди число 'b': "))
print(dif_numbers(a, b))