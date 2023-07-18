'''
Decorator

Allows behaviour to be added to an object dynamically. It provides a flexible alternative to subclassing for extending the functionality of an object without modifying its structure. The pattern follows the principle of "Open-Closed Principle" by allowing classes to be easily extended with new behaviours without modifying their existing code.

Example:
In the example, each addition to the coffee changed the description and added to the price, without changing the original object (simple_coffee).
'''

from abc import ABC, abstractmethod


class Coffee(ABC):

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


class SimpleCoffee(Coffee):
    def __init__(self, cost):
        self.cost = cost

    def get_cost(self):
        return self.cost

    def get_description(self):
        return "Simple Coffee"


class CoffeeDecorator(Coffee, ABC):
    def __init__(self, coffee):
        self.coffee = coffee

    def get_cost(self):
        return self.coffee.get_cost()

    def get_description(self):
        return self.coffee.get_description()


class MilkDecorator(CoffeeDecorator):
    def get_cost(self):
        return self.coffee.get_cost() + 0.5

    def get_description(self):
        return self.coffee.get_description() + ", Milk"


class CaramelDecorator(CoffeeDecorator):
    def get_cost(self):
        return self.coffee.get_cost() + 1.0

    def get_description(self):
        return self.coffee.get_description() + ", Caramel"


simple_coffee = SimpleCoffee(3.00)
milk_coffee = MilkDecorator(simple_coffee)
caramel_milk_coffee = CaramelDecorator(milk_coffee)

print(caramel_milk_coffee.get_description())
print(caramel_milk_coffee.get_cost())

# original object
print(simple_coffee.get_description())
print(simple_coffee.get_cost())
