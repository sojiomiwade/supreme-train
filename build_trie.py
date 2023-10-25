class Trie:

    def __init__(self, val=None):
        self.val: Optional[int] = val
        self.kids = {}

    def insert(self, word: str) -> None:
        '''
                     .
                   /
        tree: o-a-t-m-.
              c i 
        '''            
        n = len(word)
        curr = self
        for idx in range(n):
            ch = word[idx]
            if ch not in curr.kids:
                curr.kids[ch] = Trie(ch)
            curr = curr.kids[ch]
        curr.kids[None] = Trie(None)

    def _search(self, word: str, isprefix: bool) -> bool:
        '''
                     .
                   /
        tree: o-a-t-m-.
              c i 
        '''
        n = len(word)
        curr = self
        idx = 0
        while idx < n and curr and word[idx] in curr.kids:
            curr = curr.kids[word[idx]]
            idx += 1
        return idx == n and (isprefix or None in curr.kids)

    def search(self, word: str) -> bool:
        return self._search(word, False)

    def startsWith(self, prefix: str) -> bool:
        return self._search(prefix, True)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)