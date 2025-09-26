fruits = ['apple','banana','mango']
print(fruits[0:2])
print(fruits[:2])
print(fruits[0:])
print(fruits[1:10])



list1=[1,2,3]
list2=[1,2,3]
list3=list1


print(list1 == list2)  # compares the vslue
print(list1 is list2)  # 
print(list3 is list1)



countnub = [1,2,3,3,3,3,4,4,]
print(countnub)
print(countnub.count(3))


allowedcountries = ['ind','pak','sri','uk']
newcountry = 'xyz'
if newcountry in allowedcountries:
    print("allow")
else:
    print("not allowed")