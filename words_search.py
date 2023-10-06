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

