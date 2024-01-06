class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        cur=self.root
        for ch in word:
            if ch not in cur:
                cur[ch]={}
            cur=cur[ch]
        cur[None]={}
        
    def search(self, word: str) -> bool:
        def search(cur: Dict, idx: int) -> bool:
            if idx==len(word):
                return None in cur
            ch=word[idx]
            if ch != '.':
                if ch in cur:
                    return search(cur[ch],idx+1)
                return False
            if ch=='.':
                found=False
                for curch in cur.values():
                    found=found or search(curch,idx+1)
                return found
        return search(self.root,0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)