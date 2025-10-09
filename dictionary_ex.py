name = "shiv"
age = 25
company = "xyz"
hobbies = ['kabbadi', 'swimming','singing']
salary = 10000
ismarried = True

person = {
    "name":"shiv",
    "age": 25,
    "company":"xyz",
    "hobbies":['kabbadi', 'swimming','singing'],
    "salary":1000,
    "ismarried":True

}
print(person['name'],person['age']) # extract the values

persons = [{ "name":"shiv",
    "age": 25,
    "company":"xyz",
    "hobbies":['kabbadi', 'swimming','singing'],
    "salary":1000,
    "ismarried":True

},
{
     "name":"Mahadev",
    "age": 25,
    "company":"xyz",
    "hobbies":['kabbadi', 'swimming','singing'],
    "salary":1000,
    "ismarried":True
}

]

shivinfo,mahadevinfo= persons
print(mahadevinfo["hobbies"])
