import pandas as pd
from scipy import stats

data = pd.read_csv('advertisement_clicks.csv')


clicks_A = data[data['advertisement_id'] == 'A']['action']
clicks_B = data[data['advertisement_id'] == 'B']['action']

print(clicks_A.mean(), clicks_B.mean())

t, p = stats.ttest_ind(clicks_A, clicks_B)
print(t, p)