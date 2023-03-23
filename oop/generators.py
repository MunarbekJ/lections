gen = (x for x in range(10))
print(gen)
#<generator object <genexpr> at  0x7f6837f426c0>

def generator(n):
    for i in range(1, n+1):
        yield i**2

print(generator(10))
# 

gen = generator(10)
print(next(gen))#1
print(next(gen))#4
print(next(gen))#9
print(next(gen))

for i in generator(5):
    print(i)

gen = generator(15)
while True:
    try:
        print(next(gen))
    except StopIteration:
        break
    #9
# 16
# 25
# 36
# 49
# 64
# 81
# 100
# 121
# 144
# 169
# 196
# 225

class IterInt(int):
    def __iter__(self):
        for i in str(self):
            yield int(i)


def __len__(self):
    return len([i for i in self])

def __getitem__(self, index):
     return [i for i in self][index]

a = IterInt(1234567)



for i in a:
    print(i)

print(8 in a)
print(8 in a)
# print(len(a))
# print(len(a))
print(a[-1])
print(a[1:4])
print(a+1)


string1 = 'abcefsre'
string2 = 'dfjf'
print(string1 >string2)

class MyStr:
    def __init__(self, string):
        self.string = string

    def __eq__(self, other):
        return len(self) == len(other)

def __ge__(self, other):
        return len(self) >= len(other)
def __le__(self, other):
        return len(self) <= len(other)
def __gt__(self, other):
        return len(self) > len(other)
def __ne__(self, other):
        return len(self) != len(other)

string1 = MyStr('hello')
string2 = MyStr('abcde')
print(len(string1))

class A:
    attr1 = 'aaa'

    def __getattribute__(self, name):
        print("__getattribute__:", name)
         

    def __setattr__(self, name, value):
        print("__setattr__", name, value)

    def __delattr__(self, name):
        print("__gellattr__", name)
        return super()
# obj = A()

print(A.__dict__)
obj = A()
print(obj.__dict__)# {}
obj.attr1 = 'bbb'
print(obj.__dict__)
del obj.attr1
print(obj.attr1) # 'aaa'


getattr(obj, 'attr') # obj.attr1
setattr(obj, 'new_attr', 'ccc')# obj.new_attr = 'ccc'
delattr(obj, 'new_attr') # del obj.new_attr
hasattr(obj, 'dsgh') # True/False