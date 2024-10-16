from abc import ABC, abstractmethod
import random


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        return "удар мечом"

class Bow(Weapon):
    def attack(self):
        return "выстрел из лука"

class Axe(Weapon):
    def attack(self):
        return "мощный удар топором"


class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} сменил оружие на {weapon.__class__.__name__}")

    def attack(self):
        if self.weapon:
            print(f"{self.name} атакует: {self.weapon.attack()}")
        else:
            print(f"{self.name} безоружен")


class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} получает урон! Текущее здоровье: {self.health}")
        if self.health <= 0:
            print(f"{self.name} побежден!")


def fight(fighter, monster):
    damage = random.randint(10, 30)
    print(f"{fighter.name} атакует монстра {monster.name}")
    fighter.attack()
    monster.take_damage(damage)


fighter = Fighter("Рыцарь")
monster = Monster("Дракон", 100)

sword = Sword()
bow = Bow()
axe = Axe()

fighter.change_weapon(sword)
fight(fighter, monster)

fighter.change_weapon(bow)
fight(fighter, monster)

fighter.change_weapon(axe)
fight(fighter, monster)
