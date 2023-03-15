# """
# миксины- классы, которые будут исползоватся для наследствания 
# но от Миксины не создаются обьекты 
# 2 миксины - классы - ghbvtcb? rjnjhst cke;fnm lkz hfcibhtybz aeyrwbjyfkf rkfccf
# """
# # от максинов нельзя создавать обьекты ,
# # поскольку миксины - не сомастоятельные классы 
# # при наследование миксины должны идти в первую очередь 
# class WalkMixin:
#     def walk(self):
#         print('я могу ходить')

# class SwinMixin:
#     def swim(self):
#         print('я могу плыть')


# class Human(WalkMixin, SwinMixin):
#     NameError = 'человек'

#     def talk(self):
#         print('я могу говорить')

# class Fish(SwinMixin):
#     name = 'рыба'

# # class Exocoetidae(SwinMixin, FlyMixin):
#     name = 'летучая рыба'


# # class Duck(WalkMixin, SwinMixin, FlyMixin):
#     name = 'утка'

# obj = Human()
# setattr(obj, 'new_attribute', 'hello wirld')
# # print(dir(obj))
# print(obj.name)
# print(obj.new_attrbute)
# # obj = Exocoetidae()
# obj.fly()
# obj.swim()
# objects = [Human(), Fish(), Exocoetidae(), Duck()]
# for obj in objects:
#     # print(obj.name)
#     attrs = ['fly', 'swim', 'walk', 'talk']
#     for attr in attrs:
#         if hasattr(obj, attr):
#             method = getattr(obj, attr)
#             method()
# obj = Duck()
# print(hasattr(obj, 'fly'))
# method = getattr(obj, 'fly')
# num1 = 5
# func
# obj = Human()
# obj.talk()
# obj.walk()

# hasattr - функция которая принимает обект и названия атрибута Возвращает True  если у обекта ест такой атрибут (метод) 
# delattr - функция которая принимает обьекты и названия атрибута  возвращения значение атрибута 

# setattr - функция которая принимает обьекты названия атрибута и значение атрибута добавляет в обекты новый атрибут  или перезапишет одноименный 