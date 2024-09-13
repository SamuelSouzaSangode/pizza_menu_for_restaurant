import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)

pop = pd.read_csv('state-population.csv')
'''state/region | ages | year | population'''
areas = pd.read_csv('state-areas.csv')
'''state | area'''
abbrevs = pd.read_csv('state-abbrevs.csv')
'''state | abbreviation'''


merged = pd.merge(pop, abbrevs, how='outer', left_on='state/region',
right_on='abbreviation').drop(['abbreviation'], axis=1)

colunas_nulas = merged.isnull().any()

valores_nulos = merged[merged['population'].isnull()]

merged.loc[merged['state'].isnull(), 'state/region'].unique()

merged.loc[merged['state/region']=='PR', 'state'] = 'Puerto Rico'
merged.loc[merged['state/region']=='USA', 'state'] = 'United Stades'

final = pd.merge(merged, areas, on='state', how='left')

colunas_nulas_final = final.isnull().any()

areas_nulas = final['state'][final['area (sq. mi)'].isnull()].unique()

final.dropna(inplace=True)

data2010 = final.query("year == 2010 & ages == 'total'")

data2010.set_index('state', inplace=True)

density = data2010['population'] / data2010['area (sq. mi)']

density.sort_values(ascending=False, inplace=True)

print(density)
print(density.tail())
