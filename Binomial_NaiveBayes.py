import string
from collections import defaultdict
import re
from collections import Counter
import operator
import math
from nltk.corpus import stopwords

def unique_list(data):
    seen, result = set(), []
    for item in data:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
    
with open('train', 'r') as myfile:
    documents=myfile.read().splitlines()
    
print(documents)

documents = [''.join(c for c in s if c not in string.punctuation) for s in documents]


for j in range(len(documents)):
    print(type(documents[j]))


    str = documents[j].split()
    newStr = ''
    for i in Counter(str).keys():
        newStr = newStr + i + " "
        
    documents[j]=newStr
    print(documents[j])
    
    
    
    
    
    
    


speakers_all =list()
    
speakers_all=[i.split()[0] for i in documents]
    
print(len(speakers_all))
    
No_of_docs = len(speakers_all)

counts = Counter(speakers_all)
print(counts['sanders'])

    
speakers = []
for i in speakers_all:
    
    if i not in speakers:
        
        speakers.append(i)

print (speakers)
print(len(speakers))

    
    
speakers_speech=dict((el,None) for el in speakers)    


for item in documents:
    temp=item.split(' ', 1)[1]
    first_word=item.partition(' ')[0]
    if(speakers_speech[first_word]==None):
        speakers_speech[first_word]=temp                   
            
    else:
        speakers_speech[first_word]+=temp
lenght_dictionary = dict()                    
for k,v in speakers_speech.items():
    x = v.split()
    lenght_dictionary[k]=len(x)
    
    

print(lenght_dictionary)    

with open('test', 'r') as minefile:
    full_test_documents=minefile.read().splitlines()    
    

speakers_test =list()
    
speakers_test=[i.split()[0] for i in full_test_documents]

full_test_documents = [''.join(c for c in s if c not in string.punctuation) for s in full_test_documents]


for j in range(len(full_test_documents)):
    print(type(full_test_documents[j]))


    str = full_test_documents[j].split()
    newStr = ''
    for i in Counter(str).keys():
        newStr = newStr + i + " "
        
    full_test_documents[j]=newStr
    print(full_test_documents[j])
speakers_test_speech=dict((el,None) for el in speakers)    

test_documents=list()

for item in full_test_documents:
    temp=item.split(' ', 1)[1]
    first_word=item.partition(' ')[0]
    test_documents.append(temp)
    if(speakers_test_speech[first_word]==None):
        speakers_test_speech[first_word]=temp                   
            
    else:
        speakers_test_speech[first_word]+=temp
    

listnew=[]
for i in documents:
    wordss=i.split()
    listnew+=wordss
vocab=[]
for word in listnew:
    if word not in vocab:
        vocab.append(word)
        
V=len(vocab)
print(V)


i=0
counter=0
for item in test_documents:
    prob=0
    min=0
    sum=0
    prob=[]
    class_of_doc=None
    for speaker in speakers:
        wordList = re.sub("[^\w]", " ",  item).split()
        #print(speaker)
        #print(speakers_speech[speaker])
        N=lenght_dictionary[speaker]
        sum=math.log(counts[speaker])-math.log(No_of_docs)
        
        
        #print(wordList)
        for word in wordList:
            count=0
            #print(word)
            if word in speakers_speech[speaker]:
                count= speakers_speech[speaker].count(word)
            sum+=math.log(count+0.1)
            sum-=math.log(N+V*0.1)
            
        
            
            
        if(sum<0):
            prob=math.fabs(sum)
        if(min==0):
            min=prob
            class_of_doc=speaker
            
        elif(prob<min):
            min=prob
            class_of_doc=speaker

      
    tempo=full_test_documents[i]
    tempo=tempo.partition(' ')[0]  

    if(class_of_doc==tempo):
        counter=counter+1
    i=i+1
    
    
print(counter)
print(len(test_documents))       
accuracy=counter/len(test_documents)

print(accuracy*100)
         
    
            
   
