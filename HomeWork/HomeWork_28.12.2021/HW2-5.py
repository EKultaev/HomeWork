my_list = [7, 5, 3, 3, 2]

new_rating = int(input('Введите значение рейтинга: '))
inserted = False
for index, elem in enumerate(my_list):
    if new_rating > elem:
        my_list.insert(index, new_rating)
        inserted = True
        break

if not inserted:
    my_list.append(new_rating)

print(my_list)