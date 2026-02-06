/**
kdssadbutsad
   ^
sad
ans 3
use r = 26
then sad = s*r^0 + a*r^1 + d*r^2
adb = (cur - s*r^0) // radix + b*r^2

check kds for a match
then in loop remove a char, add a char, then check for a match
then sad = s*r^0 + a*r^1 + d*r^2
adb = (cur - s*r^0) // radix + b*r^2
nd abc
hs kabc
    ^
nval a*r^0 + b*r^1
ab
**/
func strStr(hs string, nd string) int {
    if len(hs) < len(nd) { return -1 }
    nval, shsval, r := 0, 0, 26
    var a byte = 'a'
    next := 1
    for i := 0; i < len(nd); i++ {
        nval += int(nd[i]-a) * next
        shsval += int(hs[i]-a) * next
        next *= r
    }
    if nval == shsval { return 0 }

    next /= r
    for i := 1; i < len(hs)-len(nd)+1; i ++ {
        shsval  -= int(hs[i-1]-a)
        shsval /= r
        shsval += int(hs[i+len(nd)-1]-a) * next
        if shsval == nval {return i}
    }
    return -1
}