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

