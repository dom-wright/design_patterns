'''
Iterator

A behavioural design pattern that separates the iteration logic from the structure of the collection. The benefit of this, is that it allows for multiple simulataneous iterations of the underlying data structure to occur (each iterator maintains its own position within the collection). If you did not separate the iterator logic and defined __iter__ and __next__ inside the MyCollection class, all existing iter objects would progress each other's pointers each time next is called.

It also means multiple different iteration strategies can be made available on the collection. See how an additional reverse iterator is created below. Note however that 'for' loops can only operate on the iterator defined in the __iter__ method.
'''

from abc import ABC, abstractmethod


class Iterator(ABC):

    @abstractmethod
    def __next__(self):
        pass

    @abstractmethod
    def has_next(self):
        pass


class ForwardIterator(Iterator):

    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __next__(self):
        if self.has_next():
            current = self.collection[self.index]
            self.index += 1
            return current
        else:
            raise StopIteration

    def has_next(self):
        return self.index < len(self.collection)


class ReverseIterator(Iterator):
    def __init__(self, collection):
        self.collection = collection
        self.index = len(collection) - 1

    def __next__(self):
        if self.has_next():
            current = self.collection[self.index]
            self.index -= 1
            return current
        else:
            raise StopIteration

    def has_next(self):
        return self.index >= 0


class MyCollection:

    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return ForwardIterator(self.data)

    def reverse_iterator(self):
        return ReverseIterator(self.data)


collection = MyCollection([1, 2, 3, 4, 5])


my_iterator = iter(collection)
my_iterator2 = iter(collection)

print("Standard Iterators")
print(next(my_iterator))
print(next(my_iterator2))

print(next(my_iterator))
print(next(my_iterator2))

# Reverse iteration
reverse_iterator = collection.reverse_iterator()
reverse_iterator
print("Reverse Iterator")
print(next(reverse_iterator))
print(next(reverse_iterator))
print(next(reverse_iterator))
