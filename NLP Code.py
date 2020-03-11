import nltk
import string

import pandas as pd


from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
nltk.download('stopwords')
nltk.download('punkt')

 

F = open('L:\\JR\\JR.txt','r') 
raw =  F.read() 

print(raw)


content = raw.lower()
print(content)


  
stop_words = set(stopwords.words('english')) 
  
word_tokens = word_tokenize(raw) 

nlp_words = nltk.FreqDist(word_tokens)
nlp_words.plot(30)



for s in string.punctuation:
  content =content.replace(s,'')
  
word_tokens1 = word_tokenize(content) 
  
filtered_sentence = [w for w in word_tokens1 if not w in stop_words] 
  
filtered_sentence = [] 
  
for w in word_tokens1: 
    if w not in stop_words: 
        filtered_sentence.append(w) 




  
#print(word_tokens) 
#print(filtered_sentence) 




nlp_words = nltk.FreqDist(filtered_sentence)
nlp_words.plot(30)








wordfreq = []
for w in word_tokens:
    wordfreq.append(word_tokens.count(w))
    
List = str(word_tokens)    
Frequencies = str(wordfreq)
    
d = {'Month':List,'Day':Frequencies}

df = pd.DataFrame(d, index=[0])
df

#-------------------------------------------------------------------------


wordfreq1 = []
for w in filtered_sentence:
    wordfreq1.append(filtered_sentence.count(w))
    
List1 = str(filtered_sentence)    
Frequencies1 = str(wordfreq1)
    
d1 = {'Month':List1,'Day':Frequencies1}

df1 = pd.DataFrame(d1, index=[0])
df1







