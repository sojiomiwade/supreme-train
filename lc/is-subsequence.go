// for each char in s, it will exisit in t, while not advancing the i and j pointers -- O(m+n), O(1)
// a b c 
//       i
//             j
// a h b g d c q
// a b c d
//       i
//               j
// a h b g d c q
// while looping on t. if we can get out of s, return true. otherwise return false
// i.e., i == len(s)

// q
// i 
//     j
// a e b
func isSubsequence(s string, t string) bool {
    m,n := len(s), len(t)
    if m == 0 { return true}
    for i,j := 0,0; j < n; j = j+1 {
        if s[i] == t[j] {
            i++
            if i == m {
                return true
            }
        }
    }
    return false
}