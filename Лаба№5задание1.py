#1.Базовый класс и методы
class Book():
    title = ''
    author = ''
    year = 0
    def get_info(self):
        print('Название книги:', self.title, '; Автор:', self.author, '; Год издания:', self.year)
x = Book()
x.title = 'Оно'
x.author = 'Стивен Кинг'
x.year = 1986
x.get_info()