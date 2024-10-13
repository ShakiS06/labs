#3.Создание и использование пакетов
import my_module
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = input('Выберите операцию: ')
if c == 'Сложение':
    print(my_module.sum(a, b))
elif c == 'Вычитание':
    print(my_module.sub(a, b))
else:
    print('Такой операции нет')