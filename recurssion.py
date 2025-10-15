def print_nums(n):
    for item in range(1,n+1):
        print(item) 

print_nums(20)

# recurssion method

start = 1
def print_nums1(num):
    global start
    print(start)
    start +=1
    if start<=num:
      print(num)
print_nums1(10)

def hello(name):
    print("hello",name)
hello1 = hello
hello1("mahi")
def add(a,b):
    print("a and b = ",a+b)
    print("addtion of two numbers:")
def sub(a,b):
    print("sub of two  numbers:")
    print(a-b)
def mul(a,b):
    print("mul of two  numbers:")
    print(a*b)
def div(a,b):
    print("div of two  numbers:")
    print(a/b)

# function with defult value
operation_dict = {
    "add":add,
    "sub":sub,
    "mul":mul,
    "div":div,
}

def calculate1(a=10,b=20,optype="add"):
    call_back =operation_dict[optype]
    call_back(a,b)
 
calculate1(100,100,"mul")


def whileloopfunc(num):
    a = 0
    while a<=num:
        print("while:",a)
        if a%2 == 0:
            print(a)
        a+=1
whileloopfunc(20)