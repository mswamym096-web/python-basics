l1 = ['a','b','c','d']
w,x,y,z =l1
print(w,x,y,z) #unpacking all tems and adding them in w x y zrespectively
config = ('root','1234','http//google.com')
username, password,url =config 
print(username, password,url)

config1 = ('root1','1234','http//google.com')
*dummy,url =config1 # last one will be added to url and reaming first  2 will be ignord
print(url)


fruits = ['apple','water','juice','banana',]
fruits,*liquid,fruitlast = fruits
print(fruits,liquid,fruitlast)