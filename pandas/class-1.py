import pandas as pd  # importing pandas as pd
series = pd.Series([1,2,3,4,5]) # creation of pandas series using pd.Series
print(series) # prits SERIES
print(type(series)) # its show type of series


user ={
    "name": ['x','y','z','a','b','c'],
    "email":['x@','y@','z@','a@','b@','c@']
}

udf = pd.DataFrame(user)
print(udf)
print(udf.head()) # print top 5 items
print(udf.tail()) # print last top 5 items



employee ={
    "name": ['x','y','z','a','b','c'],
    "email":['x@','y@','z@','a@','b@','c@'],
    "age":[29,30,28,31,32,34],
    "salary":[50000,55000,60000,45000,50450,65000]
}
emp = pd.DataFrame(employee)
print(emp)
print(emp.head())
print(emp.tail())
