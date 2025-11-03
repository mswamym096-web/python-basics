import pandas as pd

users = {
    "id":[1,None,2,3,4,5,5,None],
    "name":['a',None,'b','c','d','e','e',None]
}

userdf = pd.DataFrame(users)


# nullvalues = userdf.isnull()
# print(nullvalues)
start = 20
skipval = 6
userdf['age']= [i for i in range(start,start+len(userdf))]
userdf['agedesc']= [i for i in range(start,start-len(userdf)*skipval,-skipval)]
 
userdf = userdf.dropna()

userdf = userdf.drop_duplicates()
start = 20
userdf['age1'] = [i for i in range(start,start+len(userdf))]


userdf['id'] = userdf['id'].astype("int")
userdf["age"]= [20,22,23,24,25,55]


userdf['lname']= userdf['name'].apply(lambda name: len(name))

userdf['updateage']= userdf['age'].apply(lambda age: age+1)


userdf['name'] = userdf['name'].apply(lambda name:name.upper())
 
userdf['age'] = ['even' if i % 2 == 0 else 'odd' for i in userdf['age']]


print(userdf)


data2= {
    "name":['a','b','c','d','e','f','g'],
    "marks":[20,50,30,40,36,60,75]
}
marksdf = pd.DataFrame(data2)

# marksdf['result']= marksdf['marks'].apply(lambda mark:"fail" if mark<35 else'pass')
def grade(marks):
    if marks<35:
        return 'fail'
    elif marks>=35 and marks<=45:
        return 'B'
    elif marks>45 and marks<=60:
        return 'A'
    else:
        return 'O'


marksdf['result']=marksdf['marks'].apply(grade)
print(marksdf) 