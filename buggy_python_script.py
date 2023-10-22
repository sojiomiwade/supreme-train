'''
this program has some bugs. fix it to be correct
'''
#original
def reverse(values):
    N = len(values) 
    for i in range(N):
        values[i] = values[N - i]
        values[N - i] = values[i]     
    return values


#fixed
def reverse(values):
    values = values[:]
    N = len(values) 
    for i in range(N // 2): # 0 ->
        # 0, 3 = 3, 0
        values[i], values[N - 1 - i] = values[N - 1 - i], values[i]
    return values
  
if __name__ == '__main__':
    values = [1, 20, 53, 42]
    rev = reverse(values)
    for i in range(len(values)):
        print("Reverse:", values[i], "->", rev[i])
