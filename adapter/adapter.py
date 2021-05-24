import pandas as pd
import numpy as np

data = pd.read_csv('../scraper/data/zandparts.csv')

data['Brand'] = data.apply(lambda row : " ".join(row['Brand'].split()).split(',')[-1].strip(),axis=1)
data['Category'] = data.apply(lambda row : " ".join(row['Category'].split()).split(',')[-1].strip(),axis=1)
data['Quality'] = data.apply(lambda row : " ".join(row['Quality'].split()).split(',')[-1].strip(),axis=1)
data['PartNo'] = data.apply(lambda row : " ".join(row['PartNo'].split()).split(',')[-1].strip(),axis=1)
data['Price'] = data.apply(lambda row : float(" ".join(str(row['Price']).split()).split(',')[-1].strip().split('EUR')[0].replace(' ','')),axis=1)
data['Description'] = data.apply(lambda row : " ".join(row['Description'].split()).strip(),axis=1)
data['Description'] = np.where(data['description_alternative'].notna(),data['description_alternative'],data['Description'])
data.drop('description_alternative',axis=1,inplace=True)
data['ImageLinks'] = 'https://www.zandparts.com' + data['ImageLinks']
data = data[data['Price'].notna()].reset_index(drop=True)
data = data[data['Name'].notna()].reset_index(drop=True)

print(data.info())

data.to_csv('../result.csv')

