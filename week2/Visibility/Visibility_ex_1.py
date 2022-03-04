class Product(object):
    pass

class Inventory(object):
    def __init__(self):
        self.__items = [] #it's Private variable that declaration object can't approach

    def add_new_item(self, product):
        if type(product) == Product:
            self.__items.append(product)
            print("new item added")
        
        else:
            raise ValueError("Invalid Item")

    def get_number_of_items(self):
        return len(self.__items)


my_inventory = Inventory()
my_inventory.add_new_item(Product())
my_inventory.add_new_item(Product())
print(my_inventory.get_number_of_items())

my_inventory.add_new_item(object)   #Invalid Item


            