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
input: [1,5,11,7], 6
Expected: [[7,1],[11,5]]

wait, just put all the elements in a dict! and just check for y+k. done!
if so, then put [y+k,y]

input 1 5 11 7 | k 6
        y
have {1 5 11 7}
ans [[7 1] [11 5]]
'''
def find_pairs_with_given_difference(arr, k):
  ans=[]
  have=set(arr)
  for y in arr:
    if y+k in have:
      ans.append([y+k,y])
  return ans