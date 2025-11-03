import pandas as pd

company = {
    "dep":['IT','HR','IT','FINANCE','IT','FINANCE','HR'],
    "emp":['a','b','b','d','e','r','f'],
    "salary":[20000,30000,45000,50000,48000,None,None]
}

com = pd.DataFrame(company)
com['salary']=com.groupby('dep')['salary'].transform(lambda salary: salary.fillna(salary.mean()))
print("salary_fillna")
print(com)
com = com.groupby("dep").max()
com['avg'] = com.groupby('dep')['salary'].transform('max')
print(com)

result = com.groupby(['dep']).agg({ 
       "salary":['max']
       
})
print(result)


result['avg'] = result.groupby('dep')['salary'].transform('sum')
print(result)
# result.columns = ['salary_min', 'salary_max', 'salary_mean', 'salary_median']
# result = result.astype("int")
