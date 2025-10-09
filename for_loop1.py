fruits = ['apple','mango','banana']
#getting index and item
for index,items in enumerate(fruits):
    print(index,items,len(items))

#stopping loop based on condition and using keyword break
numbers = [1,2,3,4,5,6,]
for z in numbers:
    if z==2:
        print("yes stopped")
        break
    print(z)

# # finding items 
searchitem = 2
isfound = False
for num in numbers:
    if searchitem== num:
   # isfound True
      print("found")
      break

    #if isfound :
    #    print("found")
    #else:
    # print("not found")
    
#     # stopping loop

# names = ['a','b','c','d']
# for char in names:
#     print(char)
#     if char=='c':
#         break
# print("filtering words....")
# dirtywords = ['fk','sx','as']
# username = ['fk','hi','as','hello','bye']
# for u  in dirtywords:
#     print(u)

# #printing table any numbers
# tablenumupto = 20
# tablenum = 20
# for n in range(1,tablenumupto+1):
#     print(n*tablenum)