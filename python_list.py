# # fruits = ["apple","orange","banana"]
# # myfruits = fruits
# # myfruits.append("graphes")
# # print(id(fruits))
# # print(id(myfruits))


# # numbers = [1,2,3,4,5,6,7]
# # print(len(numbers))



# fruits = ["apple","orange","banana"]

# print(fruits.index("orange"))
# # add new item at end.
# fruits.append("watermelon")
# fruits.insert(0,"yyz")
# # remove item from list
# fruits.remove("apple")
# # it always removes last item
# fruits.pop()
# print(fruits)
# print(len(fruits))

#  nested list.
# mixed_fruits =[['apple',['a','b']],['nuts','almonds'],['water','juice'],"hi",True]
# first_item = mixed_fruits[0]
# mixed_fruits[0][1][1]="c"
# print(first_item[1])
# # print(mixed_fruits[0][1][1])


 
# alfbets =[['a','b','d'],['c','d'],['e','f']]
# print(alfbets)


# alfbets[0].append(['a1','a2'])
# print(alfbets)
# alfbets[0][1]="c"
# print(alfbets)


# roll_no = [1,2,3,4,5,6,7,8,9]
# print(roll_no)
# print(max(roll_no))
# print(min(roll_no))
# roll_no.short()
# print(roll_no)
# print(roll_no[2])
# names=['mahi','shivu','shree','ram']
# print(names)
# print(names[0:3])
# print(len(roll_no))
# print(rool_no[0:5])
# print(roll_no[-1])
# names.append('santhu')
# print(names)
# names.insert(2,'ravi')
# print(names)
# names[2]='pavan'
# print(names)
# names.remove('shree')
# print(names)
# names.pop()
# print(names)
# print(names.pop())



dm =[['ram','shivu','sangu'],['ravi','ramesh'],['pavan','raghu'],"hi",True]
print(dm)
dm[1].append(['siddu','balaji'])
dm[0].append('karadi')
dm[0].extend(['ranga','sunil'])
print(dm)