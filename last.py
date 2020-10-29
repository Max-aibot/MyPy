from random import randint, shuffle


class Game:
    def __init__(self):
        self.card = 'Cards are not generated... Not yet...'
        self.name = 'Game script'
        self.kegs = list(range(1, 90))
        self.win_chek = 15

    def gen_card(self):
        shuffle(self.kegs)
        lis1, lis2, lis3 = sorted(self.kegs[0:5]), sorted(self.kegs[5:10]), sorted(self.kegs[10:15])
        """Такой странный способ генерации карточек остался от прошлых версий,
        когда я использовал совсем другой подход. Но оно работает и поэтому здесь"""
        for i in range(4):
            lis1.insert(randint(0, 7), ' ')
            lis2.insert(randint(0, 7), ' ')
            lis3.insert(randint(0, 7), ' ')

        self.card = ((
                '_______________________\n' +
                str(lis1) + '\n' +
                str(lis2) + '\n' +
                str(lis3) + '\n' +
                '_______________________')
        ).replace(',', '').replace("'", '').replace("[", ' ').replace("]", ' ')

        return f' {self.name}\n{self.card}'

    def card_check(self):
        for i in self.get_keg():
            chek = input('Зачеркиваем? ').title()

            if str(i) in self.card.split() and chek == 'Y':
                self.card = self.card.replace(' ' + str(i) + ' ', ' () ')
                print(self.name + '\n' + self.card)
                self.win_chek -= 1

                if self.win_chek == 0:
                    print('Вы выйграли!')
                    with open('lot_data.txt', 'a+') as data:
                        data.write(self.name + ' 1\n')
                    return False

                return i

            elif str(i) not in self.card.split() and chek == 'Y':
                print('Такого числа нет в вашей карте!\nВы проиграли!')
                with open('lot_data.txt', 'a+') as data:
                    data.write('Computer' + ' 1\n')
                return False

            elif str(i) in self.card.split() and chek != 'Y':
                self.card = self.card.replace(' ' + str(i) + ' ', '>>' + str(i) + '<<')
                print(self.name + '\n' + self.card)
                print('Ошибочка!\nВы проиграли!')
                with open('lot_data.txt', 'a+') as data:
                    data.write('Computer' + ' 1\n')
                return False

            else:
                print(self.name + '\n' + self.card)
                return i

    def get_keg(self):
        shuffle(self.kegs)
        for i in self.kegs:
            self.kegs.remove(i)
            print('Следующий боченок: ' + str(i))
            yield i

    def card_check_ai(self, i):
        if 37 == randint(1, 100):
            print('Вы выйграли!\nКомпьютер ошибся!\n(Что странно...)')
            return False

        if str(i) in self.card.split():
            self.card = self.card.replace(' ' + str(i) + ' ', ' X ')
            print(self.name + '\n' + self.card)
            self.win_chek -= 1

            if self.win_chek == 0:
                print('Вы проиграли :(\nКомпьютеру везет больше.')
                with open('lot_data.txt', 'a+') as data:
                    data.write(self.name + ' 1\n')
                return False
        else:
            print(self.name + '\n' + self.card)


class Player(Game):
    def __init__(self):
        super().__init__()
        self.name = 'Computer'


class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = input('Как тебя зовут? ').title()
        try:
            with open('lot_data.txt', 'x+'):
                pass
        except FileExistsError:
            pass
        with open('lot_data.txt', 'a+') as data:
            if self.name in data.read():
                print(f'С возвращением {self.name}!')
                data.writelines(self.name + '\n')
            else:
                print(f'Добро пожаловать {self.name}')
                data.writelines(self.name + '\n')

    def get_player_stat(self):
        with open('lot_data.txt') as data:
            a = data.read()
            games_played = a.count(self.name)
            wins = a.count(self.name + ' 1')
            pc_wins = a.count('Computer 1')
            print(f'{self.name} сыграл {games_played} раз\nВыйграно {wins} игр\nКомпьютер выйграл {pc_wins} раз')


"""Start"""

start = input('Добро пожаловать в игру "Лото"\n\nНачинаем?\n(Y) для старта, (Enter) - выход, (H) - правила.\n').upper()

if start == 'H':
    print('Вы играете с компьютером. У каждого игрока есть одна карточка, создаваемая случайным образом.\n'
          'В процессе игры выпадают случайные бочонки от 1 до 89. Задача - зачеркивать числа на своей карточке.'
          'Первый игрок зачеркнувший все числа выигрывает, игра ведется до первой ошибки')

elif start == 'Y':
    player_h = Human()
    player_c = Player()
    print(player_h.gen_card())
    print(player_c.gen_card())
    z = 0
    while z < 89:
        ans = player_h.card_check()
        if ans is False:
            break
        else:
            chek_pc = player_c.card_check_ai(ans)
            if chek_pc is False:
                break
        z += 1
    player_h.get_player_stat()
else:
    print('See you...')
