class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = float(speed)
        self.color = str(color)
        self.name = str(name)
        self.is_police = bool(is_police)
        print(f'Машина {self.name} создана')

    def go(self):
        print(f'Car {self.name} riding')
        self.speed += 60

    def stop(self):
        print(f'Car {self.name} stopped')
        self.speed = 0

    def move(self):
        direction = input('Where to go? ')
        print(f'Car {self.name} turned in {direction}')
        if self.speed > 60:
            print('Over speed!')

    def get_info(self):
        print(f'Машина: {self.name}\nЦвет: {self.color}\nСкорость: {self.speed}\nМашина полиции: {self.is_police}')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')


car = Car(0, 'white', 'Honda', 1)
car.go()
car.get_info()
print(car.is_police)


class TownCar(Car):

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}' if self.speed < 60 else f'Текущая скорость: {self.speed}, тормозите')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}' if self.speed < 40 else f'Текущая скорость: {self.speed}, тормозите')


class PoliceCar(Car):
    pass


work = WorkCar(0, 'blue', 'GAZ', 0)
town = TownCar(0, 'yellow', 'Volga 21', 0)

work.go()
work.show_speed()

town.get_info()
