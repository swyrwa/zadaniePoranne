from teamwork.teamwork.liczba import Number

class ZeroAbsolutne(Number):

    def __init__(self):
        self.wartosc = 0

    def reklama(self):
        print("Ucz sie do cholery!")

    def __str__(self):
        print("Jestem Zerem!")


y = ZeroAbsolutne()
print(y.reklama())
print(y)