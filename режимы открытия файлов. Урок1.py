class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        prods_str = str (f'{self.name}, {self.weight}, {self.category}')
        return prods_str

class Shop:
    def __init__(self):
        self.__file_name = open('products.txt', 'a')
        self.__file_name.close()

    def get_products(self):
        get_file = open('products.txt', 'r')
        name_prod = get_file.read()
        get_file.close()
        return name_prod

    def add(self, *products):
        for product in products:
            if str(products) not in self.get_products():
                file = open('products.txt', 'a+')
                file.write(f'{str(product)}\n')
                file.close()
            else:
                print(f'Продукт {product} уже есть в магазине')


s1 = Shop()
p1 = Product('Spaghetti', 3.4, 'Groceries')
p2 = Product('Potato', 50.5, 'Vegetable')
p3 = Product('Potato', 5.5, 'Vegetable')
print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())

