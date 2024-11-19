class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        prods_str = str (f'{self.name}, {self.weight}, {self.category}')
        return prods_str

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r+')
        prod_str = file.read()
        file.close()
        return prod_str

    def add(self, *products):
        get_file = self.get_products()
        for i in products:
            if self.get_products().find(f'{i.name},') == -1:
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()
            else:
                print(f'Продукт {i.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Spaghetti', 3.4, 'Groceries')
p2 = Product('Potato', 50.5, 'Vegetable')
p3 = Product('Potato', 5.5, 'Vegetable')
print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())

