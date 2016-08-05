import json
import nltk
from nltk import FreqDist
from nltk.corpus import stopwords


stopwords = nltk.corpus.stopwords.words('english')
f = open('input.txt','rU')
raw = f.read()
raw_encode = json.dumps(raw)
tokens = nltk.word_tokenize(raw_encode)
text = nltk.Text(tokens)
content = [w for w in text if w.lower() not in stopwords if w.isalpha()]
frdist=FreqDist(content)


rank = sorted(frdist.items(),key=lambda k:k[1],reverse=True)
with open ('output_without_stopwords.txt','a') as csvfile:
    for a in rank:
        csvfile.write(str(a)+'\n')
