from dateutil.parser import parse
from datetime import *
import read
df=read.load_data()
def hours(data):
    hour_tm=parse(data)
    return(hour_tm.hour)
df['hours']=df['submission_time'].apply(hours)
print(df['hours'].value_counts())