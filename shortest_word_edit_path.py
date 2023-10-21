start  ---  x ------- stop
       \
        y
0      inf  1            2

dfs(G, start, stop)
    func min_distance(curr, count)
        if curr == stop
            return count
        currmin = node_count
        for nb in nbs of curr that aren't colored
            color[nb] = true
            currmin = min(node_count, min_distance(nb, count + 1))
            color[nb] = false
        return currmin

    color[*] = false
    return min_distance(start, 0)
    


'''
Shortest Word Edit Path
Given two words source and target, and a list of words words, find the length of the shortest series of edits that transforms source to target.

Each edit must change exactly one letter at a time, and each intermediate word (and the final target word) must exist in words.

If the task is impossible, return -1.

Examples:
source = "bit", target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
output: 5
explanation: bit -> but -> put -> pot -> pog -> dog has 5 transitions.

source = "no", target = "go"
words = ["to"]
output: -1

Constraints:
[time limit] 5000ms
[input] string source
1 ≤ source.length ≤ 20
[input] string target
1 ≤ target.length ≤ 20
[input] array.string words
1 ≤ words.length ≤ 20
[output] array.integer

make each word a node in a graph. And see if we can search from source to target. 2 words are neighbors only if they are one away from each other
time: setup: w**2 DFS: words + Edges. edges could be words **2

alternative: 
alphabet size = 128, ksi
have[word]: do i have word? just a set


s = a, w = b c d 
from source, find all possible 1 edits and see if in hash table. if so, take that route, until we get to destination
total runtime: w + n * ksi <--not quadratic in w!
increment and decrement count as we move forward or move back resp.


time: 12:18 - 
source = "bit", target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
output: 5
explanation: bit -> but -> put.    -> pot -> pog -> dog has 5 transitions.

'''
import sys
from typing import List

def shortest_path(words: List[str], source: str, target: str) -> int:
    def helper(curr, count) -> int: 
        if curr == target:
            return count
        mincount = 1 + len(words) #b a b c
        for i in range(len(curr)):
            for j in range(256):
                if chr(j) != curr[i]:
                    test = curr[:i] + chr(j) + curr[i+1:]
                    if test in have:
                        have.remove(test)
                        mincount = min(mincount, helper(test, count + 1))
                        have.add(test)
        return mincount

    have = set(words)
    res = helper(source, 0)
    if res != 1 + len(words):
        return res
    return -1

source = "bit"
target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
print(shortest_path(words, source, target)) # 5

source = "bit"
target = "put"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
print(shortest_path(words, source, target)) # 2


source = "bit"
target = "bit"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
print(shortest_path(words, source, target)) # 0

source = "bit"
target = "but"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
print(shortest_path(words, source, target)) # 1




'''
Shortest Word Edit Path
Given two words source and target, and a list of words words, find the length of the shortest series of edits that transforms source to target.

Each edit must change exactly one letter at a time, and each intermediate word (and the final target word) must exist in words.

If the task is impossible, return -1.

Examples:
source = "bit", target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
output: 5
explanation: bit -> but -> put -> pot -> pog -> dog has 5 transitions.

source = "no", target = "go"
words = ["to"]
output: -1

1 ≤ source.length ≤ 20
[input] string target, 1 ≤ target.length ≤ 20
array.string words,  1 ≤ words.length ≤ 20
[output] array.integer

can do all search dfs. if n words. then cost is d**w or f(d)
. . ./- ./-
d * (d-1) * (d-2) * (d-w) * ...  = 

can use bfs and we know when we get there
d + 2d + 4d + 8d + ...
d ( 2**(log w)) = dw
but log w can be made log(w/2)  with bidirectional search

                bit
        but ...
        /
      ...
    /
  target

time of this bfs approach: 
'''
from typing import Deque, List, Tuple
from collections import deque

#can check for uplicates iin words; all words have equal length
def find(source: str, target: str, words: List[str]) -> int:
    def process():
        res = []
        curr = target
        while curr:
            res.append(curr)
            curr = pi[curr]
        return res
        
    def oneaway(word: str, otherword: str):
        count = 0
        for cha, chb in zip(word, otherword):
            count += cha != chb
        return count == 1

    '''
    w: length of a word
    v: number of words
    d: average degree
    e: number of edges in graph
    '''
    # time : v + ew
    #      : or dvw (from perspective of d + d**2 + ... + d**lg_d(v)
    # space: w (how many nodes could get in the queue)
    #vs all dfs paths: time: d**w; space: w
    q = deque([source])
    level = 0
    marked = {source}
    pi = {source: ''} 
    while q:
        level += 1
        for _ in range(len(q)):
            parent = q.popleft()
            for candchild in words:
                if candchild not in marked and oneaway(parent, candchild):
                    q.append(candchild)
                    marked.add(candchild)
                    pi[candchild] = parent
                    if candchild == target:
                        res = process()
                        print(res)
                        return level
    return -1

source = "bit"; target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
print(find(source, target, words)) # (list), 5
#explanation: bit -> but -> put -> pot -> pog -> dog has 5 transitions.

