
result['avg'] = result.groupby('dep')['salary'].transform('sum')