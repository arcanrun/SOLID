"""
#Wrong realizations

class Oder:
    def price(self):
        pass

    def type(self):
        pass

    def count(self):
        pass

    def deleteItem(self):
        pass

    def buy(self):
        # db connection
        # pay system
        pass

    def printOrder(self):
        pass

    def save(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass
"""

# correct realization
class Order:
    def price(self):
        pass

    def type(self):
        pass

    def count(self):
        pass

    def deleteItem(self):
        pass


class OrderShare:
    def sendBy(self):
        pass


class OrderStoreData:
    def save(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass


class OrderView:
    def printOrder(self):
        pass