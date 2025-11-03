import pandas as pd


data = {
    "name":['virat','virat','rohit','dravid','sachin'],
    "country": ['india','india','africa','england','austrelia'],
    "age":[36,36,38,46,52]
     
}

data1 = pd.DataFrame(data)
print(data1) 
data1 = data1.groupby('country').count() # gives you minimum age of by country 

data1 = data1.groupby('country').agg({
    "age":['mean']
})
data1 = data1.astype("int")

print(data1)



 
