'''
        root
        |   \
        a    c
        |     \  
        p      a
      / |       \
     .  e        .           
        |         
        .        
words in it: {ape,ca,apa}
use a dict, and its keys are the next letters from the 
prefix up till now: ap-> a:{p:{a:{.}, e:{.}},<nothing>}
'''
class Trie:

    def __init__(self):
        self.root={}

    def insert(self, word: str) -> None:
        cur=self.root
        for let in word:
            if let not in cur:
                cur[let]={}
            cur=cur[let]
        cur['.']=''

    def search(self, word: str) -> bool:
        cur=self.root
        for let in word:
            if let not in cur:
                return False
            cur=cur[let]
        return '.' in cur

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for let in prefix:
            if let not in cur:
                return False
            cur=cur[let]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)