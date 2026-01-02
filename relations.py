import pandas as pd

data = pd.read_csv('kc_house_data.csv')
correlations = []

for i in data.columns:
    if i != 'date' and i != 'id':
        relation = data[i].corr(data['price'])
        correlations.append((i,relation))
print(correlations)

# 'grade' - 0.6 'sqft_above' - 0.6 'sqft_living' - 0.7