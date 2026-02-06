
a,b = 1,2
a,b = b+a,a+b
print(a==3,b==3)
c = [1,2,3]

#   1 2 3 <-- original
#   2 1 3 <-- one possible implementation (go)
#   2 2 1 <-- another one (python)
# v 1 2 3
# i 0 1 2
c[0],c[c[0]] = c[c[0]],c[0]
print(c == [2,2,1]) 
print(c != [2,1,3]) 

c = [1,2,3]
# c[1],c[0] = 1, 2
# 2 1 3
c[c[0]],c[0] = c[0],c[c[0]]
# rhs: 1 2
# lhs: c[1],c[0]
print(c == [2,1,3])

c = [2,1,3]
# -1 1 2, = -1, 2
# -1 1 3
# c[-1] # fail
c[0],c[c[0]] = -1,c[0]
print(c == [-1,1,2])
