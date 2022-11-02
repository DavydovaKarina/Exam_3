#Task_3

# Класс Company
# 1. Создайте класс Company
class Company:
# 2. Создайте статистическое свойство levels, которое будет содержать (как словарь) все уровни квалификации
#    программиста: 1:junior , 2:middle, 3:senior,4:lead
    levels={1:"junior", 2:"middle", 3:"senior", 4:"lead"}

# 3. Создайте метод _init_, внутри которого будет определены два protected свойства:
#    1._index - передается параметром 2._levels - принимает из словаря levels значения с ключом _index
    def __init__(self, index):
        if index > 4:
            index = 4       #Максимальная квалификация, если введем index больше 4х, то вернется все равно 4
        self._index = index
        self._levels = self.levels[self._index]
        print(f"Сейчас Ваш уровень: {self._levels}")
# 4. Создайте метод _level_up(), который будет переводить программиста на следующий уровень
    def _level_up(self):
        if self._index != 4:
            self._index += 1
            self._levels = self.levels[self._index]
        print(f'Вы подняли свой уровень до: {self._levels}')
#
# 5. Создайте метод is_lead(), который будет проверять, что программист достиг последней квалификации
    def is_lead(self):
        if self._index == 4:
            print('Вы достигли максимального уровеня!')
        else:
            print(f'Сейчас Ваш уровень квалификации: {self.levels[self._index]}. Вам необходимо его поднять!')
            return self._index==4
# Класс Programmer:
# 1. Создайте класс Programmer
class Programmer(Company):
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства:
#    1) name - передается параметром, является публичным
#    2) age - возраст
#    3)level – уровень квалификации на основе словаря из Company

    def __init__(self, name,age,level):
        super().__init__(level)
        self.name = name
        self.age = age

# 3. Создайте метод work(), который заставляет программиста работать, что позволяет ему становиться более
#    квалифицированным с помощью метода _level_up()

    def work(self):
        self._level_up()
#
# # 4. Создайте метод info(), который выведет информацию о вас: имя, возраст, квалификацию
#
    def info(self):
        print(self.name, self.age, self._levels)
# # 5. Создайте статический метод knowledge_base(), который выведет в консоль справку по программированию (просто
# #    любой текст).
    @staticmethod
    def knowledge_base():
        print("Вы досигли поставленной цели!")


print('Проверка по классу Company:')
obj_1=Company(1)
obj_1._level_up()
obj_1.is_lead()
print()

print('Проверка по дочернему классу Programmer:')
obj_2=Programmer('Кристина',33,1)
obj_2.info()

while obj_2.is_lead() == False:
    obj_2.work()

obj_2.info()
obj_2.knowledge_base()
