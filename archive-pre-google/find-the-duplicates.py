'''
-- how have interviewer (me) understood the problem-- explain it back
-- use lines to separate logic 
1 2 3 3 5 6 7
3 3 6 7
      i
  j
res=[3 6 7], in this case we can make set -> uniqueness
time,space: O(m+n),O(min(m,n)) 
i,j
as long as they are within bounds
  if same, advance both, keep  the res
  if the ival is smaller advance i
  otherwise advance j
'''
def find_duplicates(arr1, arr2):
  M,N=len(arr1),len(arr2)
  i=j=0
  res=[]
  while i<M and j<N:
    if arr1[i]==arr2[j]:
      res.append(arr1[i])
      i+=1
      j+=1
    elif arr1[i]<arr2[j]:
      i+=1
    else:
      j+=1
  return res

# for each element in arr2, do a binsearch in arr1
# time,space:O(n lg m),O(n)
def find_duplicates(arr1, arr2):
  M,N=len(arr1),len(arr2)
  res=[]
  
  
  for x in arr2:
    left,right=0,M-1
    
    while left<=right:
      mid=left+(right-left)//2
      
      if arr1[mid]==x:
        res.append(x)
        break
   
      if x<arr1[mid]:
        right=mid-1
      else:
        left=mid+1
        
        
  return res
        

arr1 = [1, 2, 3, 5, 6, 7]
arr2 = [3, 6, 7, 8, 20]
print(find_duplicates(arr1, arr2))