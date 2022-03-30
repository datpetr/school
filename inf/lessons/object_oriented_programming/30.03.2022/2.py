from random import randint as ran


class Student:
    def __init__(self, name, surname, number, performance):
        self.name = name
        self.surname = surname
        self.number_of_group = number
        self.GPA = sum(performance) // len(performance)

    def __repr__(self):
        return 'Имя - {} Фамилия - {} Номер групы - {} Cредний балл - {}\n'.\
            format(self.name, self.surname, self.number_of_group, self.GPA)


def generation_numb():
    a = []
    for _ in range(5):
        a.append(ran(1, 10000))

    return a


student1 = Student('Gosha1', 'Molotov1', ran(1, 100), generation_numb())
student2 = Student('Gosha2', 'Molotov2', ran(1, 100), generation_numb())
student3 = Student('Gosha3', 'Molotov3', ran(1, 100), generation_numb())
student4 = Student('Gosha4', 'Molotov4', ran(1, 100), generation_numb())
student5 = Student('Gosha5', 'Molotov5', ran(1, 100), generation_numb())
student6 = Student('Gosha6', 'Molotov6', ran(1, 100), generation_numb())
student7 = Student('Gosha7', 'Molotov7', ran(1, 100), generation_numb())
student8 = Student('Gosha8', 'Molotov8', ran(1, 100), generation_numb())
student9 = Student('Gosha9', 'Molotov9', ran(1, 100), generation_numb())
student10 = Student('Gosha10', 'Molotov10', ran(1, 100), generation_numb())

a = [student1, student2, student3, student4, student5, student6, student7, student8, student9, student10]
a = sorted(a, key=lambda n: -n.GPA)

print(*a)
