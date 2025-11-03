import pandas as pd

users = {
    "id":[1,None,2,3,4,5,5,None],
    "name":['a',None,'b','c','d','e','e',None]
}

userdf = pd.DataFrame(users)
print(userdf)
userdf["age"]= [20,22,23,24,25,36,25,85]
print(userdf)
userdf = userdf.dropna()
print(userdf)
# userdf = userdf.drop_duplicates()
# print(userdf)
userdf['age1'] = [i for i in range(20,28)]
print(userdf)

# userdf['updateage']= userdf['age'].apply(lambda age: age+1)
# print(userdf)