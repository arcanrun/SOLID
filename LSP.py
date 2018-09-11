"""
Слабое или сильноу условие означает следующее.
X слбаее Y в том случае, если X не выполняет все
ограничения, налагаемые на Y. При этом количество
поддерживаемых ограничений не имеет значения.


Пример с нарушением LSP!
Dukck и DuckToy не являются наследниками.

Контракт Duck.fly, а именно постусловие не являются равными с DuckToy.fly

"""


class Duck:
    def fly(self):
        print('flying')


class DuckToy(Duck):
    def fly(self):
        print('It cant')


def DuckTrain(duck):
    duck.fly()



if __name__ == '__main__':
    duck_1 = Duck()
    duck_2 = DuckToy()

    DuckTrain(duck_1)
    DuckTrain(duck_2)

