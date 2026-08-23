class Parent:

    def __init__(self, title):
        self.title = title

    def greet(self):


        return "Hello from parent"

class Child(Parent):

    def greet(self):
        return super().greet()+"Hello from child"+self.title


c= Child("Rahul Shetty Academy")

print(c.greet())

