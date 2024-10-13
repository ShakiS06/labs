#1. Написание простых функций
def greet(name):
    print('Здравствуйте,', name)
greet('Иванов Иван')

def square(number):
    return print(number ** 2)
square(9)

def max_of_two(x, y):
    if x > y: return x
    if y > x: return y
print(max_of_two(10, 11))
