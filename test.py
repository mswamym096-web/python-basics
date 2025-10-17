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



set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2))
print(set1)
print(set2)


set3 = {1,2,3}
set4 = {3,4,5}
print(set3.intersection(set4  ))