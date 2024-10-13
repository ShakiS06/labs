#2.Работа с конструктором
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius
circle = Circle(5)
print('Радиус равен', circle.get_radius())
circle.set_radius(1213)
print('Измененный радиус равен', circle.get_radius())