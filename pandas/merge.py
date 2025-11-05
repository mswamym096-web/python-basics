import pandas as pd

 
user_data = pd.DataFrame({
    'username': ['alice', 'bob', 'charlie', 'diana'],
    'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'diana@example.com']
})

 
product_data = pd.DataFrame({
    'username': ['alice', 'bob', 'charlie', 'diana'],
    'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor',],
   
})

usdf = pd.DataFrame(user_data)
productdf = pd.DataFrame(product_data)
mergedf = pd.merge(usdf,productdf,on="username",how="outer")
print(usdf)
print("\n",productdf)
print("\n",mergedf)
