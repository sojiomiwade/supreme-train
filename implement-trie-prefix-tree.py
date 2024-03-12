'''
         .
    r
   a 
   t c
      k
rack
   l
cur {r:{a:{c:{k:{}}, t:{None:None}}}}      
                ^
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
        cur[None]=None

    '''
            .
        r
    a 
    t c
        k
    rat
       l
    cur {r:{a:{c:{k:{}}, t:{None:None}}}}
                           ^
    '''
    def search(self, word: str) -> bool:
        cur=self.root
        for let in word:
            if let not in cur:
                return False
            cur=cur[let]
        return None in cur

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