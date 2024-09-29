#Задание 2: Работа с аргументами функций
def describe_person(name, age=30):
    a = f'Имя:{name}, Возраст:{age} лет'
    return print(a)
describe_person('Розалия Ивановна')