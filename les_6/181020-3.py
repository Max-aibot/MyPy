class Worker:
    def __init__(self, name, surname, position, income):
        wage = income
        bonus = 0
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    def change_income(self):
        """Позволяет изменить словарь с информацией о доходе"""

        wage = float(input('Размер оклада (руб.): '))
        bonus = float(input('Размер премии (руб.): '))
        self._income = {"wage": wage, "bonus": bonus}
        print('Информация о зарплате обновлена\n', self._income)


class Position(Worker):

    def get_info(self):
        print(f'Информация по сотруднику:\nИмя: {self.name}\nФамилия: {self.surname}\n'
              f'Должность: {self.position}\nДоход: {self._income}')

    def get_full_name(self):
        print(f'Сотрудник: {(self.name + " " + self.surname).title()}')

    def get_total_income(self):
        print(f'Общий доход: {sum(self._income.values())}')


worker = Position('Peter', 'Griffin', 'local fool', 50000)

worker.change_income()
worker.get_info()
worker.get_total_income()
worker.get_full_name()
