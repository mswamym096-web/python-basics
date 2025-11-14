# def validate(func):
#     def wrapper(a,b,*args, **kwargs):
#         if isinstance(a,(int,float)) and isinstance(b,(int,float)):
#             result= func(a,b,*args,**kwargs)
#             return result
#         print(f"{a} and {b} value must be integer")
#     return wrapper

def validate1(func):
    def wrapper(a,b,*args, **kwargs):
        def validateInput(val):
            if not isinstance(val,(int,float)) or isinstance(val,bool):
                print(f"{a} value must be integer")
                return False
            return True
        if not  validateInput(a) or not  validateInput(b):
            return
        
        result = func(a,b)
        return result
    return wrapper


@validate1
def add(a,b,):
    return a+b
# @validate1
# def sub(a,b,):
#     return a-b

print(add(10,10.10))
print(add(10,"10"))

# print(sub(10,10))
# print(sub(10,"10"))
        