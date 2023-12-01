from collections import Counter
'''
1. somehow remove all punctuation
doc.split() = ['practice', ..., "you'll"]
a. for each letter in a word if it doesn't fall in ascii remove it

2. build dictionary: {practice: [3,idx]}

2. use key=function(x)
practice 3, 0
makes 1, 1
perfect 2, 3
youll 1

(w,wf,)
sort(key=lambda (w,wf,oi): (wf,oi,w))
3, practice < 1 makes but
1 makes

b' a a
b a a

f={a:2, b:1}
oil={a:1, b:0}
'''
def word_count_engine(document):
  cd=[]
  for w in document.split():
    w=w.lower()
    cw=[]
    for let in w:
      if ord('a')<=ord(let)<=ord('z'):
        cw.append(let)
    cd.append(''.join(cw))
  
  freq=Counter()
  oil={}
  oi=0
  for w in cd:
    freq[w]+=1
    if w not in oil:
      oil[w]=oi
      oi+=1
  
  freql=list(freq.items())
  #print(freql)
  interm=sorted(freql,key=lambda (w,wf): (-wf,oil[w]))
  return [[w,str(wf)] for w,wf in interm]

document="b' a a"
print(word_count_engine(document))

document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
print(word_count_engine(document))
from collections import Counter
from itertools import count
def word_count_engine(document):
  doc=document.split()
  for i,w in enumerate(doc):
    doc[i]= ''.join(x for x in w.lower() if ord('a')<=ord(x)<=ord('z'))   
  freq=Counter(doc)
  res={}
  counter=count()
  for w in doc:
    if w not in res:
      res[w]=[freq[w],next(counter)]   
  res_tup=sorted(res.items(),key=lambda t: (-t[1][0],t[1][1]))
  return [[w,str(f)] for (w,(f,_)) in res_tup]
