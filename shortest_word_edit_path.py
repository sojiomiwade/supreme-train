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
    def helper(curr, count) -> int: #bit0,but1,put2
        if curr == target:
            return count
        mincount = None
        for i in range(len(curr)):
            for j in range(256):
                if chr(j) != curr[i]:
                    test = curr[:i] + chr(j) + curr[i+1:]
                    if test in have:
                        have.remove(test)
                        if not helper(test, count + 1):
                            assert mincount
                            mincount = min(count + 1, mincount)
                        have.add(test)
        return -1 if not mincount else mincount

    have = set(words)
    return helper(source, 0)

source = "bit"
target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
print(shortest_path(words, source, target))

# source = "bit"
# target = "put"
# words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
# print(shortest_path(words, source, target))


# source = "bit"
# target = "bit"
# words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
# print(shortest_path(words, source, target)) # 0

# source = "bit"
# target = "but"
# words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
# print(shortest_path(words, source, target)) # 1

