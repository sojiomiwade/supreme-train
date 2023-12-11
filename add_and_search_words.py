class WordDictionary:

    def __init__(self):
        self.root={}

    def addWord(self, word: str) -> None:
        cur = self.root
        for let in word:
            if let not in cur:
                cur[let]={}
            cur=cur[let]
        cur['done']='done'

    def search(self, word: str) -> bool:
        '''
                .  wi=3, cur={d's dict} root={b:{a:{d:{done:done}}}, c:{o:{t:{done:done}}}}
            o       b   c
            r       a   o
            .       d   t
                    .   .
        b.d and bad true
        bod = false

                    . wi=1,word=ab,cur=a dict root={a:{done:done}} 
                a
                done       
        '''
        def search(cur: Dict, wi: int) -> bool:
            if wi==len(word):
                if 'done' in cur:
                    return True
                return False
            if word[wi]=='.':
                found=False
                for dictlet in cur:
                    if dictlet != 'done':
                        found=found or search(cur[dictlet],wi+1)
                return found
            if word[wi] in cur:
                return search(cur[word[wi]],wi+1)
            return False

        return search(self.root,0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)