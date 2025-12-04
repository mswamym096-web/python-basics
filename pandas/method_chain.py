import pandas as pd


data = {
    "country": ['India','india','africa','england','Austrelia','africa'],
    "name":['a','a1','b','d','e','f'],
    "age":[36,36,38,46,52,None]
     
}

def clean_data(data):

    df = (
        pd.DataFrame(data)
        .query("age.notna()")
        .assign(age=lambda df: df["age"].astype("int"))
        .assign(country=lambda df: df['country'].str.upper())
        .assign(avarege=lambda df: df['age'].mean().astype("int"))
        .assign(totalage=lambda df: df.groupby("country")["age"].transform("sum").astype("int"))
        .sort_values(by=["country"])
        .rename(columns={"country":"c"})
        
        )
    return df
print(clean_data(data))
cleaned_df5 = clean_data(data)
cleaned_df5.to_csv("cleaned_data.csv", index=False)
 


