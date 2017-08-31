import read
from collections import Counter
df=read.load_data()
s=''
for words in df['headline']:
    s=s+str(words)+' '
s.lower()
s=s[:len(s)-1]
list_of_words=[]
list_of_words=s.split(' ')
c=Counter(list_of_words)
print(c.most_common(100))
