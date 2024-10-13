#2. Запись в файл
file = open('user_input', 'w')
x = int(input('Сколько фраз вы хотите добавить?:'))
for i in range(1, x+1):
    text = input('Введите текст: ')
    file.write(text)
    print('Записано')
file.close()