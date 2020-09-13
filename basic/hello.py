"""
    패키지, 클래스, 메소드 사용법을 익히기 위해 만든 패키지 입니다.
    test.py에서 구현했습니다.
"""

def hello():
    print("Hello, World")


class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def show(self):
        print("{}의 키는{}, 몸무게는{}".format(self.name, self.height, self.weight))

