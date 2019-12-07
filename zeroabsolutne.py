from teamwork.zadaniePoranne.liczba import Number


class ZeroAbsolutne(Number):

    def __init__(self):
        self.wartosc = 0

    def reklama(self):
        print("Ucz sie do cholery!")

    def __str__(self):
        return("Jestem Zerem!")


y = ZeroAbsolutne()
y.reklama()
print(y)
