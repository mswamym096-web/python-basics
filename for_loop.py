fruits = ['apple','mango','banana']
# loopin through each item
for fruit in fruits:
    print(fruit)

    # print len of the each item
    # print(fruit,"length is",len(fruit))

    #printing only those fruits whose len is greater then or equel to 6
    if len(fruit) >= 6:
        print(fruit)

a = 10
name = "abcd"
isvalidc = True
price = 10.50

if a == int("10"):
    print("yes")
else:
    print("no")

if int(price)== 10:
    print("yes")
else:
    print("no")

config = ("user","root","password")
print(config[2])

a,b,c = config
print(a,b,c)

fruits = ['apple','banana']
ap,ba =fruits
print(ap,ba)

company = {
    "name":"xyz",
    "revenue":100000,
    "Address":{
        "name":"abcd",
        "pincode":571111,
        "houseno":'#203',
    },
    "isproductbased":False,
    "directors":['a','b','c'],
    "discription":""

}
print(company["name"])
print(company.get('ceo','damn'))
if company['isproductbased']:
    company.update({"discription":"this is productbased"})
else:
    company.update({"discription":"this is not productbased"})
print(company['discription'])

nums = [1,2,3,4,5,6,7,1,0,20,30]
totalnums = 0
for num in nums:
    print(num)
    totalnums = totalnums+num
    totalnums += num

#print totalnums
even_values=[]
odd_values=[]

for n in nums:
    if n%2==0:
        print(n,"even")
        even_values.append(n)
    else:
        print(n,"odd")
        odd_values.append(n)
        print(odd_values,even_values)




