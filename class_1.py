class Abcd:
    def __init__(self,name,email):
        print("i am constuctor")
        self.firtsname = name
        #    self.firtsname = name is the instance variable
        self.email = email

    def print_all_info(self):
        print("hi",len(self.firtsname))
        print(self.email.upper())
        print(self.email[0:1])
        marks = 100
        salary = 10000
        msg = f"my name {self.firtsname} and my salary is {salary} and marks is {marks}"
        print(msg)
abcd = Abcd("hello wold",'a@a.com')
abcd.print_all_info()


 