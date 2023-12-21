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
print(find_and_replace(sentence, src, dest)) # "dogA"'''
In a given string, replace all strings mouse with a string dog

my_name_mouse_fish_mouse
my_name_mouse_fish_mouse
new string: my_name_dog --then move two over... and keep going
keep copying until find mouse
on mouse, copy dog. then advance i by 2
bruteforce: because space is O(n)

inplace: we do it from the left since dog is smaller than mouse

dog_se
      i
    j
dog_
i moves 5
j copies dog 
'''

from typing import List


def replace(arr: List[str]) -> List[str]:
    i=j=0
    dog='dog'
    mouse=list('mouse')
    while i<len(arr):
        if arr[i:i+5]==mouse:
            for k in range(3):
                arr[k+j]=dog[k]
            i+=5
            j+=3
        else:
            arr[j]=arr[i]
            i+=1
            j+=1
    return arr[:j]

s=list('my_name_mouse_fish_mouse')
print(''.join(replace(s)))