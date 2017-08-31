import pandas as pd
data=pd.read_csv('CRDC2013_14.csv',encoding="Latin-1")
#print(data['JJ'].value_counts())
#print(data['SCH_STATUS_MAGNET'].value_counts())
jjongender=data.pivot_table(index='JJ',values=['TOT_ENR_M','TOT_ENR_F'],aggfunc="sum")
Statongender=data.pivot_table(index='SCH_STATUS_MAGNET',values=['TOT_ENR_M','TOT_ENR_F'],aggfunc="sum")
print(jjongender)
print(Statongender)