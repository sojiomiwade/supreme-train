/*
dog, racecar, car, da
fish fid fia
sort the strings and consider only the 1st and last: append to ans until no more match

f, l: ab ac
ab de
*/
func longestCommonPrefix(strs []string) string {
    sort.Strings(strs)
    n := len(strs)
    f, l := strs[0], strs[n - 1]
    if len(l) < len(f) {
        f, l = l, f
    }
    i:=0
    for i = 0; i < len(f); i++ {
        if f[i] != l[i] {
            break
        }
    }
    return f[:i] // could panic too
}