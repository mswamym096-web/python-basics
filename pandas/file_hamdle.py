# fileobj = open("log.txt","r")
# print(fileobj.readline())
# fileobj.close()

# with open("log.txt","r") as fileobject:
#     print(fileobject.readlines())
    
# with open("log.txt","w") as fileobject:
#     fileobject.write("i am writing.....")
# with open ("log.txt","a") as fileobject:
#     for i in range(100):
#         if i%2==0:
#             fileobject.write("\n i am updating errors")
#         else:
#             fileobject.write("\n success....")
            
even_count = 0
odd_count = 0
with open("log.txt","r") as fileobject:
    for i in fileobject:
        print(i.upper())
        if "success...." in i:
            odd_count = odd_count + 1
        else:
            even_count = even_count + 1
      
    
print(even_count)
print(odd_count)

a = [1,4,7,10]
s = 0
for v in a:
    if v % 3 ==1:
        s*=v
print(s)       


    
    


    