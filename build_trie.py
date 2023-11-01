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


class Trie:

    def __init__(self):
        self.root = {}
        
    '''
        . .
       / /
    o-a-t-.
    c
    i
    word=oa
          l
    {o:{a:{.:'', t:{.:''}}}, }
          c

    '''
    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr['.'] = ''

    '''
          .
         /
    o-a-t-m-.
    word=oa
          l
    {o:{a:{.:'', t:{.:''}}}, }
          c
    '''
    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            if letter not in curr:
                return False
            curr = curr[letter]
        return '.' in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            if letter not in curr:
                return False
            curr = curr[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)from typing import Dict, List



def buildtrie(words: List[str]) -> Dict[str, Dict]:
    root = {}
    '''
            .
            /|\
            a b o-a-t-.
                    \
                    m-e-
    a b c
    o a t
    m e a

    func fw(r, c, cur: Dict)
        check trie children for a matching char to b[r][c]
        if one child found
            word += b[r][c]
            see if word so far is done: one of child's child is ''
            recurse to neighboring cells of b with the child's trie nodes
            word.pop
    '''
    for word in words:
        cur = root
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['.'] = None 
    return root

def search(root: Dict, word: str) -> bool:
    '''
            .
            /|\
            a b o-a-t-.
                    \
                    m-e-
    '''
    cur = root
    for ch in word:
        if ch not in cur:
            return False
        cur = cur[ch]
    return '.' in cur

root = buildtrie(['a', 'b', 'oat'])
print(search(root, 'oat')) # true
print(search(root, 'oa')) # false
print(search(root, 'a')) # true