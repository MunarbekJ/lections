# "-=========Ассоция=========="
# Ассоциация - принцип  ООП, В КОТОРОМ ДВА КЛАССА ДРУГ С ДРУГОМ СВЯЗАНЫ 
# АССОЦИЯ ДЕЛИТСЯ НА ДВА ПРИНЦИПА 
# 1- агрегация (более славая связь )
# 2- композиция более сильная связ 

class Battery:
    power = 100

    def charge(self):
        if self.power < 100:
            self.power = 100

class Iphone:
    def __init__(self, color):
        self.color = color
        self.battery = Battery()
        # когда мы создаем обьект от другого класса прям внутри другого - композиция 

iphone = Iphone('золотой')
del iphone
# обьект батарейки удаляется в  место обьектом Iphone

# print(iphone.battery.power)

# del iphone

# print(iphone)

class Nokia:
    def __init__(self, color, battery):
        self.color = color
        self.battery = battery
        # когда мы принимаем уже созданный вне класса обьект - агрегация 

battery = Battery()
nokia = Nokia('черный', battery)

del nokia
# удаляется только обект nokia 
# обьект батарейки  сохраняется 

print(nokia.battery)
print(battery.power)

# class A:
#     name = None
#     def get_name(self):
#         return self._name
#     def set_name(self, name):
#         self.__name = name
# john =A()
# john.get_name = None
# john.set_name = (name)
def __init__(self):
    self__name = None