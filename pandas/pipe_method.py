import pandas as pd

data = {
    "country": ['India','india','africa','england','Austrelia','africa'],
    "name":['a','a1','b','d','e','f'],
    "age":[36,36,38,46,52,None]
     
}

def loggingdata(df,msg,showedf=True):
    print(msg)
    if showedf:
        print(df)
    return df


def get_transformed_df(data):

    df = (
        pd.DataFrame(data)
        .pipe(loggingdata,"creating dataframe",False)
        .query("age.notna()")
        .pipe(loggingdata,"filtering not niulls",False)
        .assign(age=lambda df: df["age"].astype("int"))
        .assign(country=lambda df: df['country'].str.upper())
        .assign(avarege=lambda df: df['age'].mean().astype("int"))
        .assign(totalage=lambda df: df.groupby("country")["age"].transform("sum").astype("int"))
        .sort_values(by=["country"])
        .rename(columns={"country":"c"})
        .pipe(loggingdata,"final output")
        
        )
    return df
print(get_transformed_df(data))