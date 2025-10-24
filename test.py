#recusive

# def show(n):
#     if (n == 0):
#         return
#     print(n)
#     show(n-1)
# show(5)


# a = 1000
# b = 500
# diff = a - b
# print(diff)

# a = 2
# b = 4.25
# sum = a + b
# print(sum)

# for i in range(2,40,4):
#      print(i)

# a,b = 1,"2"
# c = int(b)
# sum = a + c
# print(sum)


# a = int("2")
# b = 4.25
# print(type(a))
# print(a + b)


# a = float(2.65)
# b = 4.25
# print(type(a))
# print(a + b)


# # name = input("enter your name:")
# # print("welcom",name)

# # int("5")
# # val = int(input("enter som values:"))
# # print(type(val),val)



# # int("5")
# # val = float(input("enter som values:"))
# # print(type(val),val)



# name = ("enter name:")
# age = ("enter age:")
# marks = ("enter marks:")   

# print("welcome",name)
# print("age=",age)
# print("marks=",marks)



# # list = [2, 1, 3,]
# # list.append(4)
# # print(list)

# # list = [2, 1, 3,]
# # print(list.sort(reverse=True))
# # print(list)


# # list = [2,3,4,5]
# # list.insert(1,6)
# # print(list)

# # list = [2,3,4,8,2,5]
# # list.pop(2)
# # print(list)


# tuple = (2,3,4,8,2,5)
# print(tuple.index(2)) 
 

# movies = []
# movies.append(input("enter 1st movie:"))
# movies.append(input("enter 2st movie")) 
# movies.append(input("enter 3st movie"))
 
# print(movies)

dict= {
     "name":"shree",
     "score":{
          "kan":95,
          "eng":75,
          "math":89,
          "hin":80,
          "sci":90,
          "soc":99
     },
     "age":29,
     "he_ismarried":False,
     "he_notmarried":True
}
 
# print(len(dict))
# pairs = (list(dict.items( )))
# print(pairs[1])
# print(dict.get("name"))
# print(dict.get("score"))
# dict.update({"city":"chamaraja nagar"})
# print(dict)



# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.add(3)
# collection.add("mahi")
# collection.remove(3)
# collection.add((1,2,3,4,5,6,))
# print(collection)
# collection.pop()



# set1 = {1,2,3}
# set2 = {2,3,4}
# print(set1.union(set2))
# print(set1)
# print(set2)


# set3 = {1,2,3}
# set4 = {3,4,5}
# print(set3.intersection(set4))


# count = 1
# while count <=5:
#      print("hello")
#      count+=1
   

# i = 1
# while i<=5:
#      print(apnacollege)
#      i+=1

# nums = 1
# while nums <= 100:
#      print(nums)
#      nums+=1

# nums = 100
# while nums >= 1:
#      print(nums)
#      nums -= 1

# i = 1
# while i <= 10:
#      print(19*i)
#      i += 1

# nums = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(nums):
#      print(nums[idx])
#      idx += 1

nums = (1,4,9,16,25,36,49,64,81,100)
x = 36
i = 0 
while i < len(nums):
     if (nums[i] == x):
          print("found at idex",i)
          break
     else:
          print("FINDING")
     i += 1
print("end of loop")




# nums = 1
# while nums <= 5:
#      if (nums == 3):
#         nums+=1
#         continue
#      print(nums)
#      nums+=1


#odd numbers
nums = 1
while nums <= 10:
     if (nums % 2 == 0):
        nums += 1
        continue
     print(nums)
     nums+=1


# even numbers
num = 1
while num <= 10:
     if (num % 2 != 0):
        num += 1
        continue
     print(num)
     num+=1


def cal_sum(a,b):
    sum= a + b
    print(a + b)
    return sum
cal_sum(5,10)
cal_sum(6,1025)
cal_sum(5525,10)


def calc_sum(a,b):
     return a + b

sum = calc_sum(200000,5300)
print(sum)


def cal_avg(a, b, c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg
cal_avg(92,93,95)
 

heroes = ["darshan","sudeep","shivaraj","punith","druva"]   

def print_len(list):
     print(len(list))

def print_list(list):
     for item in list:
          print(item, end=" ")


# print_list(heroes)

num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial of", num, "is", fact)
    