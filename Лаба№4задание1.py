#1.Импорт стандартных модулей
import math
x = int(input('Введите число: '))
print('Квадратный корень: ', math.sqrt(x))

#2. Отображение текущей даты и времени
from datetime import datetime
time = datetime.now()
print('Now', time)