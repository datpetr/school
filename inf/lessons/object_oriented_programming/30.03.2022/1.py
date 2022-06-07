from random import randint as ran


class War:
    def __init__(self, helth_initial=100):
        self.helth = helth_initial

    def attcak(self, numb):
        self.helth -= 20
        current = 1 if numb == 2 else 2
        return 'Игрок {} ударил {} и нанёс 20 урона и кол-во здоровья у {} - {}'.\
            format(current, numb, numb, self.helth)


unit1 = War()
unit2 = War()

while True:
    choice = ran(0, 1)

    if choice:
        print(unit1.attcak(2))
    else:
        print(unit2.attcak(1))
