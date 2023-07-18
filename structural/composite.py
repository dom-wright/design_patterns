'''
Composite (Trees)

Composes objects into a tree like structure, allowing one to work with the whole structure as if it were a single object. Each composite maintains a list of the children objects allocated to them, allowing recursive or iterative traversal.

Example:
In the example, we have boxes and different products, all items. Boxes contain content lists, which can include other boxes. Calling return_price will recursively call return_price on all its containing objects.
'''


from abc import ABC, abstractmethod


class Item(ABC):
    @abstractmethod
    def return_price(self):
        pass


class Box(Item):
    def __init__(self):
        self.contents = []

    def add_content(self, content):
        self.contents.append(content)

    def return_price(self):
        price = 0
        for item in self.contents:
            price = price + item.return_price()
        return price


class Phone(Item):
    def __init__(self, price):
        self.price = price

    def return_price(self):
        return self.price


class Charger(Item):
    def __init__(self, price):
        self.price = price

    def return_price(self):
        return self.price


class Earphones(Item):
    def __init__(self, price):
        self.price = price

    def return_price(self):
        return self.price


inner_box = Box()
inner_box.add_content(Phone(200))
inner_box.add_content(Earphones(80))

big_box = Box()
big_box.add_content(Charger(25))
big_box.add_content(inner_box)

print("Total price: " + str(big_box.return_price()))
