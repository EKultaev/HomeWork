def int_func(text):
    word = text [0].upper() + text[1:].lower()
    return word

string = input("Введите слова через пробел: ")
for word in string.split(' '):
    print(f'{int_func(word)}', end=' ')