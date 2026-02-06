// sort the string, and find the first that doesnt have a neighboring twin -- O(n lg n), O(n)
// hash table -- to find frequencies, then return the first with a freq of 1 -- O(n), O(n)
// -1 if none can be found
// l e e t

// 0 1 2 3
// f {l0 e2 t1}
// rs: e e l t
//         ind
// s:  l e e t 
// nch = l
func firstUniqChar(s string) int {
    index := map[rune]int {}
    for i,ch := range s {
        if _, ok := index[ch]; !ok {
            index[ch] = i
        }
    }
    rs := []rune(s)
    sf := func(a,b rune) int { return cmp.Compare(index[a], index[b])}
    slices.SortFunc(rs, sf)
    ind := -1
    for i := range len(s) {
        if (i-1==-1 || rs[i] != rs[i-1]) && (i+1==len(s) || rs[i] != rs[i+1]) {
            ind = i
            break
        }
    }
    if ind != -1 {
        nch := rs[ind]
        fmt.Printf("%c",nch)
        for i,ch := range s {
            if ch == nch {
                return i
            }
        }
    }
    return ind
    // f := map[rune]int {}
    // for _,ch := range s {
    //     f[ch] ++
    // }
    // for i,ch := range s {
    //     if f[ch] == 1 {
    //         return i
    //     }
    // }
    // return -1
}