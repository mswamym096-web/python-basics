import pandas as pd


data = {
    "country": ['india','india','africa','england','austrelia','africa'],
    "name":['a','a1','b','d','e','f'],
    "age":[36,36,38,46,52,54]
     
}

df = pd.DataFrame(data)
second = df['age'].nlargest(2)
print(second.min())

second1 =df['age'].nsmallest(1)
print(second1.min())

df = df.query('age > 38 and country=="africa"')
print(df)