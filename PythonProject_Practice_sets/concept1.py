class Parent:
    def greet(self):
        return "Hello from parent"

class Child(Parent):
    def hellogreet(self):
        return "Hello from child"


c= Child()
print(c.hellogreet())
print(c.greet())


