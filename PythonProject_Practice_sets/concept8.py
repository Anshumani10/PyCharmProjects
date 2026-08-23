
class Myclass():

    @classmethod
    def class_method(cls):
        return "class"

    def instance_method(self):
        return "instance"

obj1 = Myclass()
print(obj1.instance_method())
print(Myclass.class_method())



