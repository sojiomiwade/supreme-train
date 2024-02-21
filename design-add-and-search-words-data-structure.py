class WordDictionary:

    def __init__(self):
        self.root={}
    '''
    a . a .
            i
    root: {d} #{a} #{b:{} c:{} a:{}}
                            .
                        / ....
                 a 
            /    |   \  \
           b     c    a  null
           a     a    t
           d     t    t
           null  null null 
    a.a. should match two words -> true

    a.
     i
    root {null:null}
             .
            /
           a
          / |
         b null
    '''
    def addWord(self, word: str) -> None:
        cur=self.root
        for let in word:
            if let not in cur:
                cur[let]={}
            cur=cur[let]
        cur[None]=None

    def search(self, word: str) -> bool:
        def search(root: Dict, idx: int) -> bool:
            if idx==n:
                return None in root
            if word[idx]!='.':
                return word[idx] in root and search(root[word[idx]],idx+1)
            for let in root:
                if let is not None and search(root[let],idx+1):
                    return True
            return False

        n=len(word)
        return search(self.root,0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)