'''
W=len(words)
DFS: W(4**n)
walk a trie (of words) along with each cell as a start
T(n)=4**n
'''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def build_trie():
            root={}
            for word in words:
                cur=root
                for let in word:
                    if let not in cur:
                        cur[let]={}
                    cur=cur[let]
                cur['.']=word
            return root
        '''
        oabn
        otae
        ahkr
        aflv
        '''
        def findWords(r,c,root):
            if not 0<=r<m or not 0<=c<n:
                return
            if (r,c) in visited:
                return
            ch=board[r][c]
            if ch not in root:
                return
            if '.' in root[ch]:
                res.add(root[ch]['.'])
            visited.add((r,c))
            findWords(r+1,c,root[ch])
            findWords(r-1,c,root[ch])
            findWords(r,c+1,root[ch])
            findWords(r,c-1,root[ch])
            visited.remove((r,c))
                    
        m,n,W=len(board),len(board[0]),len(words)
        words,res=set(words),set()
        root=build_trie()
        visited=set()
        for r in range(m):
            for c in range(n):
                findWords(r,c,root)
        return list(res)