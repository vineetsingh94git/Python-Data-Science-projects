import pandas as pd
def load_data():
    data=pd.read_csv("/home/dq/scripts/hn_stories.csv")
    data.columns=['submission_time','upvotes','url','headline']
    
    return(data)    