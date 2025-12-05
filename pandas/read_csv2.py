import pandas as pd

try:
    df = pd.read_csv("unclean_1000_rows.csv",nrows=800)
    
    
    print(df)
except Exception as e:
    print("issue")
    print(e)
    
finally:
    print("proggram running.... as usals,nrows=500")

def clean_data(data):
    
    df (
       pd.DataFrame(data),
        df[df["age"].dropna()]
        .query("age.notna()")
        .assign(age = lambda df:df["age"].astype(int))
        .assign(name=lambda df: df["name"].str.upper())
        .assign(avrage = lambda df:df["age"].mean().astype(int))
       .assign(avgsalary=lambda df: df.groupby("name")["salary"].transform("sum").astype("int"))
    )

    # return df
print(clean_data)
df.to_csv("cleaned_data.csv", index=False)
 


