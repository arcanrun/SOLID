"""
OCP

Неправильный пример!
Использование конкретныx обектов без абстракций

Если я заxoчу использовать Http передачу данныx - придется
менять класс Mailer. Нарушает принцип OCP

class Smtp:
    def send(self, msg):
        pass
class Http:
    def send(self, msg):
        pass

class Mailer:
    def __init__(self):
        self.sender = Smtp()

    def send(self, msg):
        self.sender.send()

"""
import abc

class Sender(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def send(self):
        pass

class Smtp:
    def send(self, msg):
        print(msg)


class Http:
    def send(self, msg):
        print(msg.upper())


class Mailer:
    def __init__(self, sender: Sender):
        self.sender = sender

    def send(self, msg):
        self.sender.send(msg)


if __name__ == '__main__':
    typeSendHttp = Http()
    typeSendSmtp = Smtp()

    mailer_1 = Mailer(typeSendHttp)
    mailer_1.send('hello!')

    mailer_2 = Mailer(typeSendSmtp)
    mailer_2.send('hello!')