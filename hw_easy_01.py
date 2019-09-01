# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)



class TownCar:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def print_info(self):
        print('Машина:', self.name)
        print('Цвет:', self.color)
        print('Скорость:', self.speed)
        print('Являеется ли полицейской?:', self.is_police)

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина повернула', direction)


class SportCar(TownCar):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(TownCar):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(TownCar):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

def car_choose(choose):
    if choose == 1:
        print('-------')
        towncar.print_info()
        print('-------')
    elif choose == 2:
        print('-------')
        sportcar.print_info()
        print('-------')
    elif choose == 3:
        print('-------')
        workcar.print_info()
        print('-------')
    elif choose == 4:
        print('-------')
        policecar.print_info()
        print('-------')

def act_choose(act):
    if act == 1:
        print('Машина поехала')
    elif act == 2:
        print('Машина остановилась')
    elif act == 3:
        direction = int(input('Куда повернуть?\n'
                              '1 - Право\n'
                              '2- Лево\n'
                              'Ваш выбор: '))
        if direction == 1:
            towncar.turn('направо')
        elif direction == 2:
            towncar.turn('налево')
        else:
            pass
    else:
        pass

towncar = TownCar(60, 'red', 'Nissan', False)
sportcar = SportCar(110, 'black', 'Lamborgini', False)
workcar = WorkCar(50, 'yellow', 'Volvo', False)
policecar = PoliceCar(90, 'black', 'Mitsubishi', True)

choose = int(input('Выберите машину:\n'
                   '1 - Обычная\n'
                   '2 - Спортивная\n'
                   '3 - Рабочая\n'
                   '4 - Полицейская\n'
                   'Ваш выбор: '))
car_choose(choose)

act = int(input('Выберите действие:\n'
                   '1 - Поехать\n'
                   '2 - Остановиться\n'
                   '3 - Повернуть\n'
                   'Ваш выбор: '))
act_choose(act)