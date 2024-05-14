'''
[0, -1, -2, 2, 1], k = 1

0 -1
x  y
x - y = k

1 0 
x y

{0}
           x    y(elem)
-1: ask if 0 - -1 == 1, yes. so put 0 and 
     x(elem)  y  
and -1     -  0 = 1 ? no
regardless throw the new element 
time: O(n), space: O(n)

sort it: n lg n
then

x-y=k
             y    x               
check for elem-k,elem  and elem+k,elem

0 1 -2 | k 1
     e
have {0 1}
ans [[1,0]]
-2+1=-1
'''
def find_pairs_with_given_difference(arr, k):
  have=set()
  ans=[]
  for elem in arr:
    if elem-k in have:
      ans.append([elem,elem-k])
    if elem+k in have:
      ans.append([elem+k,elem])
    have.add(elem)
  loc={elem:i for i,elem in enumerate(arr)}
  ans.sort(key=lambda x: loc[x[1]])
  return ans