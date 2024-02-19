from typing import Dict, List,Tuple
from collections import defaultdict
'''
need to ensure apple and its descendants shore up to app
but not to ack. this is the problem.
hmm. shoring up and removing sieems hard. 

how about top-down: as we traverse trie, just put words in 
pairs list, and any downstream must add all words in pairs
when a list is going back up, remove your word. simple

ok, let's solve three problems
1. build trie
2. traverse trie 
3. print (in a structured manner) <--no, do this later
3. use pairs in traversal

Input: words = ["abs", "app", "be", "apple", "bee", "better", "bet", "absolute"]
Output: [('app', 'apple'), ('be', 'bee'), ('be', 'better'), ('be', 'bet'), ('abs', 'absolute')]

a:{p:{}}
'''
def build_trie(words: List[str]) -> Dict:
    root={}
    for word in words:
        cur=root
        for let in word:
            if let not in cur:
                cur[let]={}
            cur=cur[let]
        cur[None]=word
    return root

def printtrie(root: Dict, count: int=0):
    if None in root:
        print(count*' '+root[None])
        count+=1
    for let in root:
        if let is not None:
            printtrie(root[let],count)

'''
          root
      /          \
   a              b  
  /  \              \
 c     p             .
 |    |  \ 
 k    .   e 
 |         \
 .          l
             \
              .
root={a:{c:{}, p:{None:"ap", e:{ l: {None} } } }}
asclist [ap]
desclist_map {ap:[apel]}
'''
def findpairs(root: Dict, asclist: List[str],desclist_map):
    if None in root:
        curword=root[None]
        for asc in asclist:
            desclist_map[asc].append(curword)
        asclist.append(curword)
    for let in root:
        if let is not None:
            findpairs(root[let],asclist,desclist_map)
    if None in root:
        asclist.pop()

def find_prefix_pairs(words: List[str]) -> List[Tuple[str,str]]:
    root=build_trie(words)
    # printtrie(root)
    desc=defaultdict(list)
    ans=[]
    findpairs(root,[],desc)
    for word,desclist in desc.items():
        ans.extend([(word,descword) for descword in desclist])
    return ans

words = ["abs", "app", "be", "apple", "bee", "better", "bet", "absolute"]
print(find_prefix_pairs(words))