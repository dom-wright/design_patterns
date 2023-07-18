'''
Prototype

Allows for the cloning of an object. This is more challenging than first meets the eye, as parameters may not all be assigned through the constructor itself or may depend on system state at a particular point during the runtime. A solution is to delegate cloning to the object itself.
'''

from abc import ABC, abstractmethod
from copy import deepcopy


class Prototype(ABC):

    @abstractmethod
    def clone(self):
        pass


class MyObject(Prototype):

    def __init__(self, arg1, arg2):
        self.field1 = arg1
        self.field2 = arg2

    def __operation__(self):
        self.performed_operation = True

    def clone(self):
        obj = MyObject(self.field1, self.field2)
        obj.performed_operation = self.performed_operation
        return obj


"""ALTERNATIVE"""


class MyObject(Prototype):

    def __init__(self, arg1, arg2):
        self.field1 = arg1
        self.field2 = arg2

    def __operation__(self):
        self.performed_operation = True

    def clone(self):
        return deepcopy(self)
