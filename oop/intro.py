class Person:
    arms = 2
    legs = 2
    name = 'Nastya'

    def __init__(self, name):
        # __init__ - dunder метод,который добавляется в обьект self атрибуты, которые отличается у разных обьектов 
        self.name = name

    def walk(self):
        # self - ссылка на обьект , у которого мы вызываем данный метод
        print(self)
        print("я хожу")

# person1 = Person()
# Person.welk(person1)
# person1.walk()

# p1 = Person()
# p2 = Person()
# p3 = Person()
# print(p1.name,p2.name, p3.name)
# print(dir(Person))
# print

person1 = Person('Nastya')
person2 = Person('Nurkamila')
print(person1.name, person2.name)

# Атрибуты классаи атрибуты обьекта класса


class A:
    var1 = 'переменная класса'

    def __init__(self):
        self.var2 = 'переменная обьекта'

print(dir(A))
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1']

obj = A()
print(dir(obj))
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1', 'var2']
# A.var2
#
print(A.var1)# 'переменная класса'
print(obj.var1) # ' переменная класса'
print(obj.var2) # 'переменная обьекта'