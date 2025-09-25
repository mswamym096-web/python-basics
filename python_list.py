# fruits = ["apple","orange","banana"]
# myfruits = fruits
# myfruits.append("graphes")
# print(id(fruits))
# print(id(myfruits))


# numbers = [1,2,3,4,5,6,7]
# print(len(numbers))



fruits = ["apple","orange","banana"]

print(fruits.index("orange"))
# add new item at end.
fruits.append("watermelon")
fruits.insert(0,"yyz")
# remove item from list
fruits.remove("apple")
# it always removes last item
fruits.pop()
print(fruits)
print(len(fruits))

#  nested list.
mixed_fruits =[['apple',['a','b']],['nuts','almonds'],['water','juice'],"hi",True]
first_item = mixed_fruits[0]
mixed_fruits[0][1][1]="c"
print(first_item[1])
print(mixed_fruits[0][1][1])
