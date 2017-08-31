import read
df=read.load_data()
def sub_domain(data):
    sep=str(data).split('.')
    if len(sep)==3:
        word=sep[1]+'.'+sep[2]    
        return(word)
    else:
        return(data)
df['url']=df['url'].apply(sub_domain)    
domains=df['url'].value_counts()
for index,value in domains.items():
    print("{} : {}".format(index,value))
    