'''
Abstract factory

An abstract class is partially implemented and defines the requirements (attributes and methods) that a family of related child classes should have. In python, every abstract class is derived from the abc class of the abc module. 

Implementation:
The full pattern will have abstract classes for the family of related products, but also an abstract class for the factory that will decide and create the correct product at runtime.

Example:
In the below example, we have abstract browser and messenger classes, and an abstract factory class. There are two concrete implementations for each of these abstract classes, all interchangeable in the code as they implement the abstract interface.
'''


from abc import ABC, abstractmethod


class Browser(ABC):

    @abstractmethod
    def create_search_toolbar(self):
        pass

    @abstractmethod
    def create_browser_window(self):
        pass


class Messenger(ABC):

    @abstractmethod
    def create_messenger_window(self):
        pass


class VanillaBrowser(Browser):

    def create_search_toolbar(self):
        print("Search Toolbar Created")

    def create_browser_window(self):
        print("Browser Window Created")


class VanillaMessenger(Messenger):

    def create_messenger_window(self):
        print("Messenger Window Created")


class SecureBrowser(Browser):

    def create_search_toolbar(self):
        print("Secure Browser - Search Toolbar Created")

    def create_browser_window(self):
        print("Secure Browser - Browser Window Created")

    def create_incognito_mode(self):
        print("Secure Browser - Incognito Mode Created")


class SecureMessenger(Messenger):

    def create_messenger_window(self):
        print("Secure Messenger - Messenger Window Created")

    def create_privacy_filter(self):
        print("Secure Messenger - Privacy Filter Created")

    def disappearing_messages(self):
        print("Secure Messenger - Disappearing Messages Feature Enabled")


class AbstractFactory(ABC):

    @abstractmethod
    def create_browser(self):
        pass

    @abstractmethod
    def create_messenger(self):
        pass


class VanillaProductsFactory(AbstractFactory):

    def create_browser(self):
        return VanillaBrowser()

    def create_messenger(self):
        return VanillaMessenger()


class SecureProductsFactory(AbstractFactory):

    def create_browser(self):
        return SecureBrowser()

    def create_messenger(self):
        return SecureMessenger()


def main():
    for factory in (VanillaProductsFactory(), SecureProductsFactory()):
        product_a = factory.create_browser()
        product_b = factory.create_messenger()
        product_a.create_browser_window()
        product_a.create_search_toolbar()
        product_b.create_messenger_window()


if __name__ == "__main__":
    main()
