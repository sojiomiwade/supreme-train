'''
complexity without a trie K*mn*4**(mn)
complexity with a trie
how?
build a trie from words
then at each mxn cell, 
    follow it, until you can get to end of trie.
    add that word if you can. 
    try to get to the end of the trie
'''
import typing
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def buildtrie(words: List[str]) -> typing.Dict:
            root={}
            for word in words:
                cur=root
                for ch in word:
                    if ch not in cur:
                        cur[ch]={}
                    cur=cur[ch]
                cur[None]=word
            return root

        def findWords(r: int, c: int, root: typing.Dict):
            if None in root:
                ans.add(root[None])
            if 0<=r<m and 0<=c<n and (r,c) not in visited:
                brc=board[r][c]
                if brc in root:
                    visited.add((r,c))
                    child=root[brc]
                    findWords(r+1,c,child) 
                    findWords(r-1,c,child)
                    findWords(r,c+1,child)
                    findWords(r,c-1,child)
                    visited.remove((r,c))

        visited=set()
        m,n=len(board),len(board[0])
        trie=buildtrie(words)
        ans=set()
        for r in range(m):
            for c in range(n):
                assert not visited
                findWords(r,c,trie)
        return list(ans)