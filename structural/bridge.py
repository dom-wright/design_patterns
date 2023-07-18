'''
Bridge

A design pattern focussed on achieving decoupling, namely the  abstraction (high-level interface or entity) from its implementation (low-level details or implementation logic). This allows them to vary and develop independently. The name "Bridge" is derived from the concept of bridging or connecting two different parts of a system i.e. the abstraction and its implementation. It acts as a bridge between these two components, allowing them to work together while remaining independent.

Example:
In the example, the abstraction (building) and implementations (material, but could also be doors, window types etc) can vary independently. Materials and their properties / behaviours do not have to be defined in every building, instead they are defined in a separate class, and can be modified there when required. All this promotes code reusability and flexibility.

The pattern also facilitates the selection of different implementations at runtime e.g. a gamer defining attributes about their character or updating their stats.
'''

from abc import ABC, abstractmethod


class Material(ABC):
    @abstractmethod
    def __str__(self):
        pass


class Cobblestone(Material):
    def __init__(self):
        pass

    def __str__(self):
        return 'cobblestone'


class Wood(Material):
    def __init__(self):
        pass

    def __str__(self):
        return 'wood'


class Building(ABC):
    @abstractmethod
    def print_name(self):
        pass


class Tower(Building):
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def print_name(self):
        print(str(self.material) + ' tower ' + self.name)


class Mill(Building):
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def print_name(self):
        print(str(self.material) + ' mill ' + self.name)
