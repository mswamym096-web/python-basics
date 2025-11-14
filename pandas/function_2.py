# def logg(show,massege):
#     if show:
#         print(massege)
# logg(True,"morning")
# logg(False,"morning")



# def cal(a,b,optype):
#     if optype: 
#         print(a+b)
#     return a+b
    
# cal(10,20,True)

def calculate(c,d,opt):
    if opt == "add":
      return c + d
    elif opt == "sub":
        return c - d
    elif opt == "mul":
        return c * d
    elif opt == "div":
        return c / d
    else:
        return "invalid operaion"
print(calculate(10,20,"mul"))


def print_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

print_table(5)
 

pervalue = 100
def get_discount(totalprice,discountprice):
    result = (totalprice/pervalue )*discountprice
    print("discountprice:",result)
    print("actualprice after discount",totalprice-result)
    
     
get_discount(200,12)
get_discount(500,15)
get_discount(2000,18)   



userdatabas = [
    {
    "user":"mswamym0996@gmail.com",
    "password":95915235
    
    },
    {
          "user":"mswamym0996@gmail1.com",
          "password":9591
    },
    {
        
          "user":"mswamym0996@gmail1.com",
          "password":959152
    }
]

# def loggin(user,password):
#     if user == userdatabas["user"] and password ==userdatabas["password"]:
#         print("he is loggin")
#     else:
#         print("wrong user")
        
# loggin("mswamym0996@gmail.com",95915235)


def some_result(a,b,showresult):
    if showresult:
        return a+b
    else:
        print(a+b)
        
print(some_result(10,20,True))
print(some_result(120,20,True))


def loggin(massege,showlog):
    if showlog:
        print(massege)
loggin("hi i am good", True)

def add(a,b,show):
    c = a+b
    if show:
        print(c)
add(10,20,True)

userdatabas1 = [
    {
    "user":"mswamym0996@gmail.com",
    "password":95915235
    
    },
    {
          "user":"mswamym0996@gmail1.com",
          "password":9591
    },
    {
        
          "user":"mswamym0996@gmail2.com",
          "password":959152
    }
]

def authenticate(user,password):
    for item in userdatabas1:
        if user == item["user"] and password == item["password"]:
            print("login successfull")
            break
        else:
            print("invalid")
  
authenticate("mswamym0996@gmail.com",95915235)






     
   

 


