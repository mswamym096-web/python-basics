class Abcd:
    def __init__(self):
        print("i am constructor")
        self.a = 10
        self.b = 20
    def hi(self):
        print("hi....")
    def addtion(self):
        print(self.a+self.b)

abcd = Abcd()
abcd.addtion()
abcd.hi()