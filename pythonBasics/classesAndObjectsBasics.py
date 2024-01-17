class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


class Student(Person):
    def __init__(self, name, age, std):
        super().__init__(name, age)
        self.std = std

    def __str__(self):
        return f"{super().__str__()}{self.std}"


p1 = Student("John", 36, 1)

print(p1)
