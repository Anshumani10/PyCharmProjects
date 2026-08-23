class calculator:
    number = 100 #Class variables
    #Default constructor

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("I am called automatically when an object is created")

    def getdata(self):
        print("I am executing class")

    def add(self):
        return self.a + self.b + self.number


obj = calculator(2,3) #Syntax to create objects in python
obj.getdata()
print(obj.add())

obj2 = calculator(4,5) #Syntax to create objects in python
obj2.getdata()
print(obj2.add())





