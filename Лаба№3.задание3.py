#3. Запись в файл
try:
    with open('dengi.txt','r') as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print('Файл не найден')
