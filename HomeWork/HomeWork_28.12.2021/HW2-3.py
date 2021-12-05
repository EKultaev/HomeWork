num_month = input("Введите номер месяца в виде целого числа: ")

a, b, c, d = 'Зима', 'Весна', 'Лето', 'Осень'

month_dict ={'1':a, '2':a, '3':b,'4':b,'5':b,'6':c,'7':c,'8':c,'9':d,'10':d,'11':d,'12':a}

print(month_dict[num_month])

season_list = [a, a, b, b, b, c, c, c, d, d, d, a]

print(season_list[int(num_month)-1])

