'''
In a given string s, replace all mouse with dog

I am a mouse. She knows I eat mouses for dinner!
l
             r
       dog
repeatedly putting s[r] into s[l] as long as we don't have mouse at r
when we see a mouse, dump dog at l
then l advances len(dog), r advances len(mouse)
rinse and repeat
new string is s[:l]
after k iterations l is standing on index k (so is k+1 long)


I am a mouse.  <--s
I am a dog.e.  <--buf
             r
           l
'''
def replace_bigger_with_smaller(s: str):
    MOUSE,DOG=[x for x in 'mouse'], [x for x in 'dog']
    biglen,smalllen=len(MOUSE),len(DOG)
    buf,l,r=list(s),0,0
    while r<len(buf):
        if buf[r:r+biglen]==MOUSE:
            buf[l:l+smalllen]=DOG
            l+=smalllen
            r+=biglen
        else:
            buf[l]=buf[r]
            l,r=l+1,r+1
    return ''.join(buf[:l])

s='In a given string s, replace all mouse with dog'
print(replace_bigger_with_smaller(s))

s='I am a mouse. She knows I eat mouses for dinner!'
print(replace_bigger_with_smaller(s))
