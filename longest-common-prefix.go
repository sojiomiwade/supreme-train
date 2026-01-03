// # flight
// # flighhhh <-- don't matter
// # flow
// # flower
// # sh <-- wrench
// # a simple way: sort the list, and only consider the 1st and last elems
// # O(nm lg n)
// # in consider: move forward, and break when not equal, return ans
// fl
//  i
// flk
// ans 2
func longestCommonPrefix(strs []string) string {
        n := len(strs)
        ans := 0
        sort.Strings(strs)
        a, b := strs[0], strs[n - 1]
        for i := range len(a) {
            if a[i] == b[i] { 
                ans++ 
            } else {
                break
            }
        }
        return a[:ans]    
}

