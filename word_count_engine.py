'''
orig_ord
case insensitive -- just to lower the whole thing to start?
strip puncation out 

document a b c b' a
doc  a b c b a
splitdoc  [a b c b a]
orig_ord {a0 b1 c2}
count {a2 b2 c1}
words [(a2) (b2) (c1)]
  print(splitdoc)
  print(count)

'''
import collections


def word_count_engine(document):
  doc=''.join(ch for ch in document.lower() if ch==' ' or ch.isalnum())
  splitdoc=doc.split()
  orig_ord={}
  for i,word in enumerate(splitdoc):
    orig_ord.setdefault(word,i)
  count=collections.Counter(splitdoc)
  words=list(count.items())
  aux=sorted(words,key=lambda x: (-x[1],orig_ord[x[0]]))
  ans=[[s,str(freq)] for s,freq in aux]
  return ans

doc='a b c b; a'
print(word_count_engine(doc))