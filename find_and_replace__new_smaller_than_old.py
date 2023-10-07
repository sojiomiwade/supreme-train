'''
In a given string s, replace all mouse with dog
9:48 -- 10:21 = 81 - 48 = 33 m


a[l] = a[r]
r+=1
while r < len(sentence)
if sen[r:r+len(src)] == 'mouse'
    sen[r:r+(len(dst)] = 'dog'
    move r src count
    move l dst count
else
    sen[l] = sen[r]
    move r and s by 1

a[i..i+3] = dog

newlen = len(sen) - 2*(len(src)-len(dest))
check if substr == mouse
if so, 
put in array list
we can replace from front since dest string is less than src

I gave a mouse a good mouse.
                            r
                        l
I gave a dog a good dog.
'''
def find_and_replace(sentence: str, src: str, dest: str) -> str:
    def change_one_pattern() -> None:
        for i in range(len(dest)):
            lis[l+i] = dest[i]
    
    def match() -> bool:
        return sentence[r:r+len(src)] == src

    lis = list(sentence)
    l = r = 0
    while r < len(sentence):
        if match(): #0:5
            change_one_pattern()
            r += len(src)
            l += len(dest)
        else:
            lis[l] = lis[r]
            l += 1
            r += 1
    return ''.join(lis[:l])

sentence = 'mouseA' #dogA ... 
sentence = 'I gave a mouse a good mouse.'
src, dest = 'mouse', 'dog'
print(find_and_replace(sentence, src, dest)) # "dogA"