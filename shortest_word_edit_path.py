from collections import deque
def shortestWordEditPath(source, target, words):
  '''
  BFS  to guarantee shortest path, with count variable
  oneaway means every let the same except one
  bit
  but bat
  dont forget marked
  for each neighbor that isn't in the queue, mark it upon putting it there
  '''
  def oneaway(w,ow):
    if len(w)!=len(ow):
      return False
    count=0
    for x,y in zip(w,ow):
      if x!=y:
        count+=1
    return count==1
  
  count=0
  q=deque([source])
  marked=set([source])
  while q:
    for i in range(len(q)):
      word=q.popleft()
      if word==target:
        return count
      for otherword in words:
        if otherword not in marked and oneaway(word,otherword):
          marked.add(otherword)
          q.append(otherword)
    count+=1
  return -1

source = "bit"
target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
print(shortestWordEditPath(source, target, words)) # 5