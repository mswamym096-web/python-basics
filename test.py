#recusive

# def show(n):
#     if (n == 0):
#         return
#     print(n)
#     show(n-1)
# show(5)


a = 1000
b = 500
diff = a - b
print(diff)

# a = 2
# b = 4.25
# sum = a + b
# print(sum)

for i in range(2,40,4):
     print(i)

a,b = 1,"2"
c = int(b)
sum = a + c
print(sum)


a = int("2")
b = 4.25
print(type(a))
print(a + b)


a = float(2.65)
b = 4.25
print(type(a))
print(a + b)


# name = input("enter your name:")
# print("welcom",name)

# int("5")
# val = int(input("enter som values:"))
# print(type(val),val)



# int("5")
# val = float(input("enter som values:"))
# print(type(val),val)



name = ("enter name:")
age = ("enter age:")
marks = ("enter marks:")   

print("welcome",name)
print("age=",age)
print("marks=",marks)



list = [2, 1, 3,]
list.append(4)
print(list)

list = [2, 1, 3,]
print(list.sort(reverse=True))
print(list)