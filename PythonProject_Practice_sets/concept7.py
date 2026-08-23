class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"my name is {self.name} and my age is {self.age}")

person1 = Person("Rahul", 20)
person1.greet()

num = [3, 2, 6, 1]
print(num[::-1])

