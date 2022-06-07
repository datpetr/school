class Pet:
    def __init__(self, name, fur, color):
        self.name = name
        self.fur = 'Да' if fur else 'Нет'
        self.color = color

    def __str__(self):
        return f'Животное: \n\tИмя: {self.name}\n\tШерсть: {self.fur}\n\tЦвет: {self.color}\n'


class Cat(Pet):
    def sound(self):
        print('Мяу')


class Dog(Pet):
    def sound(self):
        print('Мяу')


cat = Cat('Garfild', True, 'Orange')
print(cat)
cat.sound()