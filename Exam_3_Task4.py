# Task_4

# Создайте класс на тему животных.
# Используйте статические и динамические переменные, дочерний (1 или более) классов на конкретное животное.
# Публичные и приватные методы.
# Полиморфизм (одинаковые названия методов info в обоих классах, которые выводят информацию о животных, либо о
# конкретном животном данного класса).
# Создайте объекты каждого класса и обратитесь к каждому методу.
# Напишите один staticmethod, один classmethod, к которым также обратитесь.

class animals():
    predatory_animals = "Хихные животные"
    herbivores = "Травоядные животные"

    def __init__(self, herb):
        self.herb = herb

    def vnimanie(self):
        if self.herb == self.herbivores:
            print("Животное можно кормить! В клетке находиться травоядное животное")
        else:
            print("Подходить к клетке и кормить животное нельзя! В клетке хищник")

    def _print(self):  # защищенный метод
        print("Погода сегодня хорошая для прогулки в зоопарке!")

    def print1(self):
        self._print()

    @classmethod
    def welcome(cls):
        print("Добро пожаловать в наш зоопарк")

    @staticmethod
    def forbidden():
        print("Залазить в клетку к животным ЗАПРЕЩЕНО!!!")


class hare(animals):
    def __init__(self, name, tip):
        super().__init__(tip)
        self.name = name

    def info(self):
        print(f"Имя животного {self.name} - это заяц, он является травоядным животным")


class cow(animals):
    def __init__(self, name, tip):
        super().__init__(tip)
        self.name = name

    def info(self):
        print(f"Имя животного {self.name} - это корова, она является травоядным животным")


print()
print("Проверка по классу animals:")

obj = animals("Травоядные животные")
animals.welcome()       # метод класса
obj.print1()
obj.vnimanie()
obj.forbidden()         # статистический метод еще его можно вызвать animals.forbidden()
print()
print("Проверка по дочернему классу hare:")
animals1 = hare("Пушок", 'Травоядные животные')
animals1.info()
print()
print("Проверка по дочернему классу cow:")
animals2 = cow("Зорька", 'Травоядные животные')
animals2.info()
