'''
perfect makes practice
ecitcarp sekam tcefrep
practcise makes perfect

1. reverse the arr
2. reverse each token: find the end of a token, reverse, then set start to end+2

ab cde
cde ab  
       s
       e
cde ab <-- exp
'''
def reverse_words(arr):
  def loc_reverse(start, end):
    i,j=start,end-1
    while i<j:
      arr[i],arr[j]=arr[j],arr[i]
      i+=1
      j-=1
      
  arr.reverse()
  start=end=0

  while start<len(arr):
    while end<len(arr) and arr[end]!=' ':
      end+=1
    loc_reverse(start,end)
    start=end=end+1
  return arr