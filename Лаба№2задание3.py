#3. Использование функций для решения алгоритмических задач
def is_prime(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
        else:
            return True
print(is_prime(77))
