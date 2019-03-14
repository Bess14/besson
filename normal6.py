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


class Person:
    def __init__(self, name, health, armor, damage):
        self.name = name
        self.health = health
        self.armor = armor
        self.damage = damage

    def _calc_damage(self, enemy):
        return self.damage / enemy.armor

    def attack(self, enemy):
        enemy.health -= self._calc_damage(enemy)


class Player(Person):
    pass


class Enemy(Person):
    pass


class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start(self):
        last_attacker = self.player

        while self.player.health > 0 and self.enemy.health > 0:
            if last_attacker == self.player:
                self.enemy.attack(self.player)
                last_attacker = self.enemy
            else:
                self.player.attack(self.enemy)
                last_attacker = self.player

        if player.health > 0:
            print('Игрок', player.name, 'победил.')
        else:
            print('Игрок', enemy.name, 'победил.')


player = Player('Кирилл', 100, 2.8, 17)
enemy = Enemy('Сергей', 100, 2.9, 16)
game = Game(player, enemy)

game.start()
