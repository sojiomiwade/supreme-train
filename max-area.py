from typing import List, Tuple
'''
1 2 3
4 5 6
7 8 9
'''
# return top down left right
def max_rect(arr: List[List[int]]) -> Tuple[int,int,int,int,int]:
    def msa():
        '''
             l    r
        2 -4 3 -2 7 -5 2 1
      0 2 -2 3 -1 6  1 3 4   
             ml
                  mr
        l is reset when sum is reset
        at any point msum beats rsum, set mr
        2 -5 3
           i
        2 -3 3*
        l
             r    
        '''
        msum=float('-inf')
        l,r=0,None
        rsum=0
        for i,x in enumerate(aux):
            if rsum<0:
                rsum=0
                l=i
            rsum+=x
            if rsum>msum:
                msum=rsum
                r=i
        return msum,l,r


    m,n=len(arr),len(arr[0])
    msum=float('-inf')
    mtop=mdown=mleft=mright=None
    for l in range(n):
        aux=[0 for _ in range(m)]
        for r in range(l,n):
            aux[:]=[aux[i]+arr[i][r] for i in range(m)]
            rsum,top,down=msa()
            print(rsum,top,down,l,r)
            if rsum>msum:
                msum,mtop,mdown,mleft,mright=rsum,top,down,l,r
    assert type(msum) is int
    assert type(mtop) is int
    assert type(mdown) is int
    assert type(mleft) is int
    assert type(mright) is int
    return msum,mtop,mdown,mleft,mright
'''
1 2 |3
3 4 |7

'''
arr = [
    [ -10,  2, -3,  1],
    [   2,  7,  0, -3],
    [  -7,  0, -2,  8],
    [  -1, -3,  1,  1],
]
# arr = [[1,2],[3,4]]
print(max_rect(arr)) # 7,1,2,1,3