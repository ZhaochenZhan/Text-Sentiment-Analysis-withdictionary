import json
import nltk
from nltk import FreqDist

f = open('input_new.txt','rU')
raw = f.read()

raw_encode = json.dumps(raw)

print ('Start to tokenize the file')
tokens = nltk.word_tokenize(raw_encode)
print ('Start to tag the tokens')
POS = nltk.pos_tag(tokens)
print ('Start to find and record the POS tag started with "N" ')
tags = [(word,tag) for (word,tag) in POS if tag.startswith('N') ]
print ('Start to write the first output file named "pos_tag_raw"')
with open('pos_tag_raw.txt','a') as csvfile:
    for a in tags:
        csvfile.write(str(a)+'\n')

print ('Start to calculate the frequency distribution of tags')        
tag_fd = nltk.FreqDist(tags)
print ('Start to sorted the outcome with counts')  
rank = sorted(tag_fd.items(),key=lambda k:k[1],reverse=True)

print ('Start to write the second output file named "pos_tag_fd"') 
with open('pos_tag_fd.txt','a') as csvfile:
    for b,c in rank:
        csvfile.write(str(b[0])+'\t'+str(c)+'\n')
