# #set is unorderd and accepts only unique values

# names = {"a","b","c","a",}
# names.add("e") # adds in the sets
# names.remove("z") # removes volve if exist other other wise throw the error
# names.discard("z") # removes value if exist other wise don't throw error
# print(names)


fruits = ["apple","mango","apple","mango"]
unique_fruits = set(fruits)
unique_list_of_fruits = list(unique_fruits)
print(unique_fruits,unique_list_of_fruits)
print(list(set(fruits)))

unique_fruits = list(set(fruits)) # coverting list to set to list
print(unique_fruits)

