import abc

"""
Жирный интрфейс

class Order(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def material(self):
        pass

    @abc.abstractmethod
    def discount(self):
        pass

    @abc.abstractmethod
    def pages(self):
        pass

    @abc.abstractmethod
    def price(self):
        pass

    @abc.abstractmethod
    def color(self):
        pass

"""


class IBook(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def pages(self):
        pass


class IClothes(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def material(self):
        pass

    @abc.abstractmethod
    def discount(self):
        pass

    @abc.abstractmethod
    def color(self):
        pass


class IOrder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def price(self):
        pass


class Book(IBook, IOrder):
    def __init__(self, pages, price):
        self.pages = pages
        self.price = price

    def pages(self):
        print(self.pages)

    def price(self):
        print(self.price())


class Cloth(IClothes, IOrder):
    def __init__(self, material, price, discount, color):
        self.material = material
        self.price = price
        self.discount = discount
        self.color = color

    def material(self):
        print(self.material())

    def price(self):
        print(self.price())

    def discount(self):
        print(self.discount)

    def color(self):
        print(self.color)


if __name__ == '__main__':
    pass