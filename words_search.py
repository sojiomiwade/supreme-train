'''
YOE, target company/level, and your interview prep progress
10y, FAANG (sr. soft).   , 

Question:
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



[a,a,a,a]
[a,a,a,a] 
[a,a,b,a]
[a,a,a,a]

aaa - 
   \
words = [aa, aaa, aaaa, aaaab, aaaaaab, aabaaaa]
4**mn

form all words possible, and keep a hash of each.
anytime you have a word, then it returns in O(1)

Input: board = [["o","a","a","n"],
                ["e","t","a","e"],
                ["i","h","k","r"],
                ["i","f","l","v"]], 1 len word or mn word ==> O(mn)
        
        words = ["oa", "oath","pea", "eat","rain"]; len(words) = w; max-length = mn
                    ^
Output: ["eat","oath"]
                                                                 each cell
DFS: for each word on the board, do a board-DFS(word): O(V+E) = O(mn   + 4*mn) => O(wmn)
    in your dfs
length of a longest word = d 
    for every cell, and every match you have worst case 4 directions to check

modularize more
work on the plan concreting. 
Trie 
'''
from typing import List


def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    def helper(r, c, count) -> bool:
        if count == len(word)-1: # 0 == 1-1
            return True

        if (r,c) in visit:
            return False
        count += 1 # 0
        match = False
        if 0<=r<len(board) and 0<=c<len(board[0]) and word[count] == board[r][c]:
            visit.add((r,c))
            match |= helper(r, c+1, count) 
            match |= helper(r+1, c, count) # (r,c)=o
            match |= helper(r-1, c, count) # (r,c)=o
            match |= helper(r, c-1, count) # (r,c)=o
            visit.remove((r,c))
        return match

    visit = set()   
    res = []
    for word in words:   #O(w)
        ismatch = False
        for r in range(len(board)): #O(m)
            for c in range(len(board[0])): #O(n)
                ismatch |= helper(r, c, count=-1) 
        if ismatch:
            res.append(word)
    return res

board = [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]]
# words = ['o', 'z'] # res = [o]
words = ["oaa", "oath","pea", "eat","rain"] #oaa, oath, eat
print(find_words(board, words))




class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def buildtrie() -> Dict[str, Dict]:
            root = {}
            for word in words:
                cur = root
                for i in range(len(word)):
                    ch = word[i]
                    if ch not in cur:
                        break
                    cur = cur[ch]
                else:
                    i += 1
                for j in range(i, len(word)):
                    ch = word[j]
                    cur[ch] = {}
                    cur = cur[ch]
                cur[''] = {}
            return root

        def printtrie(root: Dict[str, Dict], word=None) -> None:
            '''
                     .
                    /|\
             .-t-a-e q r
            '''
            if not word:
                word = []
            if not root:
                print(''.join(word))
                return
            for let in root:
                word.append(let)
                printtrie(root[let], word)
                word.pop()

        def _findWords(r, c, tch) -> None:
            '''
            cand word = eat
            0,0,tl=null,tch=(e:{}, q:{}, r:{})
            0,1,{a:{}, null:{}}
            e a
            b c
                     .
                    /|\
             .-t-a-e q r
            '''
            if not 0<=r<m or not 0<=c<n:
                return
            for tl in tch: # e, q, r / a, null
                if tl == board[r][c]:
                    word.append(tl)
                    if '' in tch[tl]:
                        found.append(''.join(word))
                    _findWords(r+1, c, tch[tl])
                    _findWords(r-1, c, tch[tl])
                    _findWords(r, c+1, tch[tl])
                    _findWords(r, c-1, tch[tl])
                    word.pop()

        found = []
        m, n = len(board), len(board[0])
        root = buildtrie()
        printtrie(root)
        word = []
        for r in range(m):
            for c in range(n):
                _findWords(r, c, root)
        return found


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
# param_3 = obj.startsWith(prefix)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def buildtrie():
            '''
            o
            oa
            b
                             .
                            / \
                           o   b
                          /
                         a
            ws=[o, o a , b]
                         w
                         c
            root = {o:{.:{},a:{.:{}}}, b:{.:{}} }
                                         t
            '''
            root = {}
            for w in words:
                t = root
                for c in w:
                    if c not in t:
                        t[c] = {}
                    t = t[c]
                t['.'] = {}
            return root
        '''
            root={o:{.:{},a:{.:{}}}}
        '''
        def printtrie(t,w):
            if '.' in t:
                print(''.join(w))
            for c in t:
                if c != '.':
                    printtrie(t[c], w+[c])

        def ts(r, c, t, w):
            if '.' in t:
                res.append(''.join(w))
                del t['.']

            if 0<=r<n1 and 0<=c<n2 and board[r][c] in t:
                brc = board[r][c]
                board[r][c] = '#'
                ts(r+1,c,t[brc],w+[brc])
                ts(r-1,c,t[brc],w+[brc])
                ts(r,c+1,t[brc],w+[brc])
                ts(r,c-1,t[brc],w+[brc])
                board[r][c] = brc

        res,t = [],buildtrie()
        n1,n2=len(board),len(board[0])
        for i in range(n1):
            for j in range(n2):
                ts(i,j,t,[])
        return res