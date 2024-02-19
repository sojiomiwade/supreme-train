'''
print-trie
build-trie
                root
              /      \ 
          a           b
       /     \          \
      null    p          a
                 \        \ 
                   p       t 
                    \       \
                     null    null
a, ap
expect : (a,app) # there is no (ap,app)
res=[(app,a)]
parents=[a]
root: {None:app} #{None:a, p:{}}  # {a:{}, b:{}}
word=[app]  
def findpairs(root,parents)
    word=[]
    if None in root:
        word.append(root[null])
        for each parent in parents
            add (root[null],parent) to res
    for let in root:
        if let is not None:
            findpairs(root[let],parents+word)

findpairs(trie,[])
'''

