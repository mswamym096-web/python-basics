# #def defination ChatGPT said:

# #in Python, a function definition is a block of code that performs a specific task and can be reused whenever needed   

# def logmessage(): # hardcode function
#     fruits = ['apple','mano']
#     print(fruits)

# logmessage()

# def add():
#     10
#     20
#     print(10+20)
# add()

# def veriables():
#     a=10
#     b=20
#     print(a+b)
# veriables()

# def sub():
#     10
#     20
#     print(10-20)
# sub()

# def multi():
#     10
#     20
#     print(10*200)
# multi()

# def div():
#     10
#     20
#     print(10/20)
# div()

# def add(x,y): # multiple parametars
#     print(x+y)

# add(1,10)
# add(2,20)


# def calc_avg(a,b,c):
#     sum= a + b + c
#     calc_avg
#     avg = sum / 3
#     print(avg)
#     return avg
# calc_avg(95,85,92)



cities = ["delhi","mumbai","channai","bangalore","mysore"]
heroes = ["shivu","sunila","prakash","ram","raj"]
# print(len(cities))
def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)


# function add accepets two params namely x,y
def add(x,y):
    return x+y

add(1,10)
add(2,10)
print(add(50,50))

def check_even(num):
    if num%2==0:
        return true
        
    return False

data = check_even(23)
print(data)


def check_even_num(num):
    if num%2==0:
        return True
        
    return False

# data = check_even_num(10)
# print(data)
isloggedin = False
isheadmin = False
def allow_access():
    if isloggedin:
        if isheadmin:
            print("he is access")
        else:
            print("you are not admin")
    else:
        print("please login")
allow_access()

# allow_access():
isloggedin = True
isheadmin = True
def allow_access_version1():
        if not isloggedin:
            print("plaese login")
            return
        
        if not isheadmin:
            print("no access")

        print("he has access")

allow_access_version1()

def accepets_more_than_zero(num):
    if num==0:
        print("invalid")
    else:
        print("your name is valid")
        for i in range(num):
            print(i)
accepets_more_than_zero(1)




def accepets_more_than_zero_version2(num):
    if num<=1:
        print(num,"is invalid please provide value more than 1")
        return
    for i in range(num):
        print(i)
accepets_more_than_zero_version2(5)


name= "mahi"
def greet (name ="guest"):
    print("hello",name)
greet()
greet(name)


name= "ravi"
def wish(name = "guest"):
    print("good mornig ", name)
wish()
wish(name)


def largest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>= a and b>=c:
        return b
    else:
        return c
print(largest(10,20,25,),"is the largest number")


def conveerter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD=", inr_val, "INR")
conveerter(456)


def calculate(a,b,optype):
    if optype == "add":
        print("addtion of two numbers:")
        print(a+b)
    elif optype == "sub":
        print(a-b)
    elif optype == "mul":
        print(a*b)
    elif optype == "div":
        print(a/b)
    else:
        print("invalid optype")
calculate(10,20,"add")


def add(a,b):
    print("a and b = ",a+b)
    print("addtion of two numbers:")
def sub(a,b):
    print("sub of two  numbers:")
    print(a-b)
def sub(a,b):
    print("mul of two  numbers:")
    print(a*b)
def sub(a,b):
    print("div of two  numbers:")
    print(a/b)

def calculate1(a,b,optype):
    if optype == "add":
        print("addtion of two numbers:")
        print(a+b)
    elif optype == "sub":
        print(a-b)
    elif optype == "mul":
        print(a*b)
    elif optype == "div":
        print(a/b)
    else:
        print("invalid optype")
calculate1(10,20,"add")


# function with defult value
def calculate1(a=10, b=20,optype="add"):
    if optype == "add":
        add(a,b)
    elif optype == "sub":
          sub(a,b)
    elif optype == "mul":
        sub(a,b)
    elif optype == "div":
        div(a,b)
    else:
        print("invalid optype")
# calculate1(10,20,"add")
# calculate1(10,20,"add")
calculate1()

# local and global scope
toatl = 10
def abcd():
    global toatl
    toatl = toatl+30
    print(toatl)

abcd()

    
