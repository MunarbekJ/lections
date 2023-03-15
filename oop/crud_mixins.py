class CreateMixin:
    def product_create(self, title, price):
        #self.__class__ - обращения к классу которое наследовался от этого миксина 
        model = self.__class__
        obj = model()
        _id = model. _id
        obj.title = title
        obj.price = price
        obj.id = id
        model.objects[_id] = obj
        model._id += 1

class ReadMixin:
    def product_detail(self, p_id):
        model = self.__class__
        obj = model.objects.get(p_id)
        print({"id": obj.id, "title": obj.title, "price": obj.price})

class UpdateMixin:
    def product_update(self, p_id, title, price):
        obj = model.objects.get(p_id)
        obj.title = title
        obj.price = price


class ProductCrud(CreateMixin, ReadMixin, UpdateMixin):
    objects = {}
    _id = 1 

crud = ProductCrud()
crud.product_create('Samsung Note 20 Ultra', 50000)
# crud.product_detail(1)
crud.product_create('Iphone 14 Pro Max', 100000)
crud.product_detail(2)
crud.product_update(2, 'Iphone 14 Pro Max', 120000)
crud.product_detail(2)