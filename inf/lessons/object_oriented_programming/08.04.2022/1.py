class Man:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Имя: {self.name} (возраст {self.age})\n'

    def return_name(self):
        return self.name

    def return_age(self):
        return self.age


class Student(Man):
    def __init__(self, name, age, university, marks):
        super().__init__(name, age)
        self.universty = university
        self.marks = marks

    def add_marks(self, mark):
        self.marks.append(mark)

    def __repr__(self):
        return f'Студент {self.return_name()}:\n\tВозраста: {self.return_age()}\n\tОценки: {list(self.marks)}\n'


class Employer(Man):
    def __init__(self, name, age, plant, salary):
        super().__init__(name, age)
        self.salary = salary
        self.plant = plant

    def change_work(self, new_plant):
        self.plant = new_plant

    def __repr__(self):
        return f'Работник {self.return_name()}:\n\tВозраста: {self.return_age()}\n\tЗавод: "{self.plant}"\n'


student1 = Student('Mark', 3, 'Oxford', [1, 2, 5, 7, 8])
print(student1)
student1.add_marks(5)
print(student1)
worker1 = Employer('Jef', 87, 'Ugolnyu', 12312312)
print(worker1)
worker1.change_work('Dnipro')
print(worker1)
