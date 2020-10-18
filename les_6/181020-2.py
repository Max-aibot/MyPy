class Road:
    def __init__(self, length, width):
        self._length = abs(int(length))
        self._width = abs(int(width))

    def mass_calculate(self, mass_one_meter, depth):
        try:
            if int(mass_one_meter) > 0 and int(depth) > 0:
                return self._length * self._width * int(mass_one_meter) * int(depth)
            else:
                return 'Incorrect values'

        except TypeError:
            return 'Incorrect values'


road = Road(20, 5000)
print(road.mass_calculate('2', 5))
