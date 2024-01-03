# Given a list of words, match all words with other words from the list that are a prefix for the word.

# Example Input and Output
# Example
# Input: words = ["abs", "app", "be", "apple", "bee", "better", "bet", "absolute"]
# Output: [('app', 'apple'), ('be', 'bee'), ('be', 'better'), ('be', 'bet'), ('abs', 'absolute')]


'''
 .
   \
     a
      \
       p
      / \
     .   p
          \
           .
'''
from typing import Dict, List, Tuple

'''
cur[.]
'''
def find_prefix_pairs(words: List[str]) -> List[Tuple[str, str]]:
    def find_prefix_pairs(cur: Dict) -> None:
        if '.' in cur:
            for parent_word in parent_words:
                res.append((cur['.'],parent_word))
            parent_words.append(cur['.'])
        for child_trie in cur.values():
            find_prefix_pairs(child_trie)
    trie=build_trie(words)
    parent_words=[]
    res=[]
    find_prefix_pairs(trie)
    return res
    

'''
                     .
                    /
                  a
                 /
                b
               /
              s
'''
def build_trie(words: List[str]) -> Dict:
    trie=root={}
    for word in words:
        root=trie
        for ch in word:
            if ch not in root:
                root[ch] = {}
            root = root[ch]
        root['.'] = word
    return trie

def print_trie(trie):
    for ch in trie:
        if ch=='.':
            print(trie['.'])
        else:
            print_trie(trie[ch])


words = ["abs", "app", "be", "apple", "bee", "better", "bet", "absolute"]    
trie=build_trie(words)
print_trie(trie)
print(trie.keys())
