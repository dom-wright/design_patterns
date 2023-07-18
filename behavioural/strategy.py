'''
Strategy

Allows you to encapsulate a set of algorithms / strategies in separate classes. The context object (user) holds a reference to the selected strategy object. The context object then delegates the algorithm's execution to that strategy object, allowing it to vary independently from the client using it.

An implementation could be to have shopping items presented in different orders based on what the user is searching by i.e. price, ratings etc. It avoids the need for multiple conditionals within the class and achieves loose coupling.
'''


class SortingStrategy:
    def sort(self, data):
        pass


class BubbleSortStrategy(SortingStrategy):
    def sort(self, data):
        print("Sorting using Bubble Sort")
        # Implementation of Bubble Sort algorithm


class QuickSortStrategy(SortingStrategy):
    def sort(self, data):
        print("Sorting using Quick Sort")
        # Implementation of Quick Sort algorithm


class SortingContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def sort_data(self, data):
        self.strategy.sort(data)


data = [5, 2, 7, 1, 8]

bubble_sort = BubbleSortStrategy()

context = SortingContext(bubble_sort)
context.sort_data(data)

quick_sort = QuickSortStrategy()

context.set_strategy(quick_sort)
context.sort_data(data)
