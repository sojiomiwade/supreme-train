'''
input:  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"

output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"], 
          ["get", "1"], ["by", "1"], ["just", "1"] ]

can just lower the whole thing and also remove punctuation
sort by frequency (descending).
when 2 are the same sort by ordinal in original string
can get ordinal using a count.
for each word
  if word not in ordlookup
    ordlookup[word]=count, 
    count ++
'''
from collections import Counter


def remove_punc(s):
  return ''.join([ch for ch in s if ch.isalnum() or ch==' ']).split()

def get_ord(s):
  ordlookup={}
  count=0
  for word in s:
    if word not in ordlookup:
      ordlookup[word]=count
      count+=1
  return ordlookup

def word_count_engine(document):
  doc=remove_punc(document.lower())
  ordlookup=get_ord(doc)
  wcount=Counter(doc)
  wtups=list(wcount.items()) # (a,2) (b,3)
  wtups.sort(key=lambda x: (-x[1],ordlookup[x[0]]))
  return [[word,str(freq)] for (word,freq) in wtups]

document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
print(word_count_engine(document))

'''
output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"], 
          ["get", "1"], ["by", "1"], ["just", "1"] ]
'''