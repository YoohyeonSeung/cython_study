def hello():
    print("Hello, World")


class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def show(self):
        print("{}의 키는{}, 몸무게는{}".format(self.name, self.height, self.weight))

