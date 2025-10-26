# lambda params: expression
#def add(a,b)
#     print(a+b)
# add(10,20)

# lambda function is ananymous function with is defined with lambda keywords

res = lambda a,b: a+b
mul = lambda x: x**2
nameupper =lambda name: name.upper()
print(res(10,20))
print(mul(10))
print(nameupper('abcdef'))


# zif is the function witch combines two or more iterators
name = ['a','b','c','d']
marks = [10,20,30]
print(list(zip(name,marks)))
for name,marks in zip(name,marks):
    print(name,marks)

evenlist = []
for i in [1,2,3,4,5,6,7]:
 if i%2==0:
    print(i)
    evenlist.append(i)
print(evenlist)


# list comprehersion is easy way to create newlist based on filter or condition 


l1 = [1,2,3,4,5,6]
filterdlist = [i for i in l1 if i%2==0]
print(filterdlist)
