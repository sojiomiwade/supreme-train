/*
can use one table of 26 chars -- map
s increments a given char, t decrements
if map is all 0 at end --> true. otherwise --> false
note: can return false imm if lengths are not the same
O(n) time, O(1) space

can sort both. then walk down. if s[i] != t[i] --> return false.
return true if never returned false.
O(n lg n) time, O(n) space

car rat
ss: acr
     i
ts: art

[26]byte
'a' - 'a'

cat
tar
freq [a c1 t r-1]
*/
func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }
    freq := [26]int{}
    for i := range s {
        freq[s[i]-'a']++
        freq[t[i]-'a']--
    }
    for _,v := range freq {
        if v != 0 {
            return false
        }
    }
    return true
    // if len(s) != len(t) {
    //     return false
    // }
    // sbs, tbs := []byte(s), []byte(t)
    // bcomp := func(a, b byte) int {
    //     return cmp.Compare(a, b)
    // }
    // slices.SortFunc(sbs, bcomp)
    // slices.SortFunc(tbs, bcomp)
    // for i := range sbs {
    //     if sbs[i] != tbs[i] {
    //         return false
    //     }
    // }
    // return true
}