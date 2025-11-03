import pandas as pd

data = {
    "emp_id": [101,102,103,104,105,106,107,108,109,110],
    "name": ["John","Priya","Ahmed","Sara","david","Meena","rakesh","Emily","Kevin","maya"],
    "department": ["IT","HR","Finance","IT","Marketing","IT","HR","Finance","Sales","IT"],
    "position": ["Developer","HR Manager","Accountant","Data Analyst","Executive","Developer","Recruiter","Financial Analyst","Sales Executive","Project Manager"],
    "salary": [60000,75000,58000,70000,45000,65000,40000,62000,48000,85000],
    "experience": [3,6,4,5,2,4,1,3,2,7],
    "joining_date": ["2020-02-10","2018-06-15","2019-09-01","2019-11-20","2021-04-05","2020-05-10","2022-01-20","2021-03-15","2021-09-25","2017-07-01"],
    "city": ["New York","Mumbai","Dubai","London","Toronto","Chennai","Delhi","New York","Sydney","San Francisco"]
}

data1 = pd.DataFrame(data)
# print(data1)

data1['name'] = data1.apply('name').apply(lambda name:name.upper())
# print(data1)

high_salary = data1[(data1['salary'] > 65000)&(data1['department']=='IT')]
print('High_salary')
print(high_salary)

IT_emp = data1[data1['department']=='IT']
print('show_only_IT_emp')
print(IT_emp)

exp = data1[(data1['department'] == 'IT') & (data1['experience']>=5)]
print('experience')
print(exp)

#groupby

avg_salary = data1.groupby('department')['salary'].mean()

# data1 = data1.groupby('deparment').agg({
#     "salary":['mean']
# })
print('avg_salary')
print(avg_salary)


df = data1["joining_date"]=pd.to_datetime(data1["joining_date"])
print(df)

df1 = data1['years_of_service'] = (pd.Timestamp("today") - data1["joining_date"]).dt.days //365

print(df1)


subset = data1[["name","department","salary"]]
print(subset)

df['avg'] = data1.groupby("department")['salary'].transform('max')
print(df)

df = data1.query('salary > 60000 and department=="IT" and position=="Data Analyst"')
print(df)
 