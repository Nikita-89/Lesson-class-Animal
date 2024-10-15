class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} издает звук.")

    def eat(self):
        print(f"{self.name} ест.")

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} чирикает.")

    def fly(self):
        print(f"{self.name} летает.")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} издает звук млекопитающего.")

    def run(self):
        print(f"{self.name} бежит.")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} шипит.")

    def crawl(self):
        print(f"{self.name} ползет.")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"Животное {animal.name} добавлено в зоопарк.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Сотрудник {staff_member.name} добавлен в зоопарк.")

    def show_animals(self):
        print(f"Животные в зоопарке {self.name}:")
        for animal in self.animals:
            print(f"{animal.name} ({animal.__class__.__name__}, {animal.age} лет)")

class Staff:
    def __init__(self, name):
        self.name = name

class ZooKeeper(Staff):
    def feed_animal(self, animal):
        if isinstance(animal, Animal):
            print(f"{self.name} кормит {animal.name}.")
            animal.eat()

class Veterinarian(Staff):
    def heal_animal(self, animal):
        if isinstance(animal, Animal):
            print(f"{self.name} лечит {animal.name}.")

zoo = Zoo("Городской зоопарк")

zoo.add_animal(Bird("Попугай", 3))
zoo.add_animal(Mammal("Лев", 5))
zoo.add_animal(Reptile("Крокодил", 7))

zoo.show_animals()

zoo_keeper = ZooKeeper("Иван")
veterinarian = Veterinarian("Анна")

zoo.add_staff(zoo_keeper)
zoo.add_staff(veterinarian)

zoo_keeper.feed_animal(zoo.animals[0])
veterinarian.heal_animal(zoo.animals[1])

