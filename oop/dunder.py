# dunder (double underscore) - методы у которых 2 - в начале  и в конце 
# магия в том , что мы не вызываем напрямую 

class A:

    def __new__(cls):
        return super().__new__(cls)
    
    def __init__(self):
        print("__INIT__")
        pass

A()
# __NEW__
#__INIT__

# __new__, __init__ - вызывается при создания обьекта 
print(dir(object))
# print(dir(A))
print(dir(int))
# __eq__>=
#__le__<=
# __lt__<
# __ne__!=
# __ad__+
# __ sub__-
#__floordiv__/
# __trudev__// 
print(A())
# <__man__.A object at 0x7mdsfnk.f'g
class A:
    def __str__(self) -> str:
        return f"<__man__.{self. __class__. __name__}"
    
print(A())
# Hello

class A:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        return self.number = number == other.number
class A:
    def __str__(self) -> str:
        return "A __REPR__"

obj1 = A(5)
obj2 = A(5)

print(obj1 == obj2)
        