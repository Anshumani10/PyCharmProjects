from oops import calculator


class child(calculator):

    num2 = 200

    def __init__(self):
        calculator.__init__(self, 2, 10)

    def get_complete_data(self):
        return self.num2 + self.number +self.add()

obj = child()
print(obj.get_complete_data())
