import pandas as pd

try:
    df = pd.read_csv("order.csv")
    
    
    print(df)
except Exception as e:
    print("issue")
    print(e)
    
finally:
    print("proggram running.... as usals,nrows=5000")

