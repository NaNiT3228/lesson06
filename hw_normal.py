# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


import random


class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _income_damage(self, damage):
        if self.health > 0:
            self.health = self.health - self.damage/self.armor
        else:
            self.health = 0
        if self.health > 0:
            print('{} получил урон и теперь имеет {} здоровья'.format(self.name, self.health))
        else:
            print('{}у был нанесен последний удар последний удар'.format(self.name))
            self.health = 0

    def punch(self, person):
        person._income_damage(self.damage)


class Player(Person):
    def __init__(self, name, health, damage, armor):
        Person.__init__(self, name, health, damage, armor)


class Enemy(Person):
    def __init__(self, name, health, damage, armor):
        Person.__init__(self, name, health, damage, armor)


class Game:
    def __init__(self, person1, person2):
        self.person1 = person1
        self.person2 = person2

    def fight(self, person1, person2):
        while person1.health > 0 and person2.health > 0:
            person1.punch(person2)
            if person2.health == 0:
                print('{} победил!'.format(person1.name))
                break
            person2.punch(person1)
            if person1.health == 0:
                print('{} победил!'.format(person2.name))


player = Player('Игрок', 100, 10, random.randint(1, 5))
enemy = Enemy('Враг', 100, 10, random.randint(1, 5))

game = Game(player, enemy)
game.fight(player, enemy)