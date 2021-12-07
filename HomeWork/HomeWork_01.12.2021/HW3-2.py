def info_user (l_name, f_name, ears, city, e_mail, tel):
     return f'{l_name} {f_name} {ears} {city} {e_mail} {tel}'

a = input("Имя: ")
b = input("Фамилия: ")
c = input("Год рождения: ")
d = input("Город: ")
e = input("Электронный адрес: ")
f = input("Номер телефона: ")
print(info_user(l_name=a, f_name=b, ears=c, city=d, e_mail=e, tel=f))