"""
OCP

Неправильный пример!

Если необxодимо добавить новый формат вывода,
например DOC, приднтся менять исxодный код



class Report:
    def __init__(self, report):
        self.report = report

    def print(self):
        if self.report == 'PDF':
            print('PDF')
        elif self.report == 'CSV':
            print('CSV')
"""
import abc


class InterfaceReport(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def print(self):
        pass


class ReportDoc(InterfaceReport):
    def print(self):
        print('DOC')


class ReportPdf(InterfaceReport):
    def print(self):
        print('PDF')


if __name__ == '__main__':
    pass