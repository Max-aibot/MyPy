class Stationery:

    def __init__(self, title):
        self.title = title
        print(f'Объект "{self.title.title()}" создан')

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print('Чернила кончились...')


class Pencil(Stationery):

    def draw(self):
        print('Грифель сломался...')


class Handle(Stationery):

    def draw(self):
        print('Краска высохла...')


stat = Stationery('Штуковина')
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

stat.draw()
pen.draw()
pencil.draw()
handle.draw()
