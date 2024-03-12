'''
can use BFS to reach target, and count along the way
neighbor(word) --> change each letter and see if it is in set(words)
  mark it visited!

source     target
bit    but cut
q [bit but cut]
count 2
visited {bit but cut}
word bit
     j
count exp is 2
'''
import collections
def shortestWordEditPath(source, target, words):
  wlen=len(source)
  count=0
  q=collections.deque([source])
  swords=set(words)
  while q:
    for i in range(len(q)):
      word=q.popleft()
      if word==target:
        return count
      for j in range(wlen):
        for k in range(26):
          oword=word[:j]+chr(97+k)+word[j+1:]
          if oword in swords:
            swords.remove(oword)
            q.append(oword)
    count+=1
  return -1