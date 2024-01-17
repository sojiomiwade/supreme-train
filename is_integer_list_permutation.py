# array of integers of size N is a permutation if 2 conditions hold:
# 1. a[i] in [0, N - 1]
# 2. all numbers appear exactly once
# first: sort, and check a[i]=i. time,space=nlg(n),n
# second: hashtable based lookup. time,space:n,n
# third: put everything in the right place: n,1
# 0 1 2 3 4 5
# 3 4 1 5 2 0
# 3 4 1 5 2 0
def is_perm(arr) -> bool:
    n=len(arr)
    for i in range(n):
        if not 0<=arr[i]<n:
            return False
        while i!=arr[i]:
            x=arr[i] # 3
            if not 0<=x<n or arr[x]==x:
                return False
            temp=arr[x] # arr[3]=5
            arr[x]=x
            arr[i]=temp
    return True

arr=[3,4,1,5,2,0]
print(is_perm(arr)) # True
arr=[3,4,1,5,2,10]
print(is_perm(arr)) # False
arr=[3,3,3,5,2,10]
print(is_perm(arr)) # False
