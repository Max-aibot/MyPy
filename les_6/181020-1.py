from time import sleep
from itertools import cycle


class LightTraffic:
    def __init__(self, color):
        self._color = color
        print('Traffic light on ' + color + ' added')

    # def running(self):
    #     while 1:
    #         print('Red light! Wait...')
    #         sleep(7)
    #         print('Yellow! Get ready...')
    #         sleep(2)
    #         print('Green! Go!\n')
    #         sleep(10)

    '''Не знаю, зачем светофору атрибут color, и зачем реализовывать смену цвета
    через cycle(), но раз задание, как у солдатов, то вот :)'''

    def running(self):
        for color in cycle(['red', 'yellow', 'green']):
            print(color)
            if color == 'red':
                sleep(7)
            elif color == 'yellow':
                sleep(2)
            else:
                sleep(10)


traffic_l = LightTraffic('Mira st.')
traffic_l.running()
