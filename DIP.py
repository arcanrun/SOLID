import abc

"""
Зависимости внутри системы строятся на основе абстракций.
Модули верхнего уровня не зависят от модулей нижнего уровня,
оба зависят от абстракции. Абстракции не должны зависеть от деталей. 
Детали должны зависеть от абстракций». Данное определение можно сократить: 
Зависимости должны строится относительно абстракций, а не деталей.

"""


class Sender(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def send(self):
        pass


class Station(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def connect(self):
        pass


class MegafonStation(Station):
    def __init__(self):
        self.name = __class__.__name__

    def connect(self):
        print(self.name)


class SmsSender(Sender):
    def __init__(self, connect):
        self.connector = connect # подключаемся к РАЗЛИЧНЫМ вышкам

    def send(self):
        self.connector.connect()
        print('sending by sms...')


class Mailer:
    def __init__(self, sndr: Sender):
        self.sender = sndr

    def send(self):
        self.sender.send()


if __name__ == '__main__':
    station = MegafonStation()
    smsSending = SmsSender(station)
    mailer = Mailer(smsSending)

    mailer.send()