class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}\n'


class Shop:
    def __init__(self):
        self.products = []

    def get_products(self):
        file = open(self.__file_name, 'r')
        data = file.read()
        file.close()
        return data

    def add(self, *products):
        for p in self.products:
            if self.get_products().find(f'{p.name},') == -1:
                print(f'Продукт {product.name} уже есть в магазине')
                return self.products.appened(products)

    def __str__(self):
        return '\n'.join(str(p) for p in self.products)


s1 = Shop()
p1 = Product('Spaghetti', 3.4, 'Groceries')
p2 = Product('Potato', 50.5, 'Vegetable')
p3 = Product('Potato', 5.5, 'Vegetable')

s1.add(p2)
s1.add(p3)
s1.add(p1)

print(p1, p2, p3)
