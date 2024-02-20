import pandas as pd

data = pd.read_csv('data2.csv')
data['Qlt*Read'] = data['Quality'] * data['Count']
data.to_csv('data.csv', index=False)
