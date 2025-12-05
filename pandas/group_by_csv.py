import pandas as pd
import matplotlib.pyplot as plt
# try:
df = pd.read_csv("users.csv")
    
    
#     print(df)
# except Exception as e:
#     print("issue")
#     print(e)
    
# finally:
#     print("proggram running.... as usals")
    

df['avg'] = df.groupby('city')['salary'].transform('mean').astype("int")


# df['avg'] = df.groupby('city')['salary'].agg(
#     mean_salary = 'mean',
#     median_salary = 'median'
    
# )





print(df)

df.to_csv('avg_salary.csv',index=False)

plt.bar(df['city'],df['avg'],color='red')
plt.xlabel('city')
plt.ylabel('avg')
plt.title('avg salary with cities')
plt.legend('right lower')
plt.show()