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
*/
func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }
    sbs, tbs := []byte(s), []byte(t)
    slices.Sort(sbs)
    slices.Sort(tbs)
    for i := range sbs {
        if sbs[i] != tbs[i] {
            return false
        }
    }
    return true
}