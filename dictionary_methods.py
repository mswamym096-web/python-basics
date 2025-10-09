  emp = {
    "name":"abcd",
    "email":"abcd@gamil.com"
}

name = emp['name']
email = emp['email']
# accessing value from the dictionary
name1 =emp.get('name')
email1 =emp.get('email')
print(name1,email1)

#updating dictionary with mobile and ismarried as key
emp['mobile']='959152365256'
emp.update({"ismarried":True,"isnotmarried":False})
print(emp)

# removing ismarried from dictionary and returns its value
value = emp.pop('ismarried')
print(emp)
print(value)

# get method
