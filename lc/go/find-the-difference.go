// put s in a set, and find the letter in that thats not in s -- n, n

// sort s and t, then find the first place they aren't the same -- n lg n, n
// d a b e c
// a b c d
//       -1
//have: [a b c d e1]
func findTheDifference(s string, t string) byte {
    have := [26]int {}
    n := len(s)
    for i := 0; i < n; i++ {
        have[t[i] - 'a']++
        have[s[i] - 'a']--
    }
    have[t[n] - 'a'] ++

    for i,v := range have {
        if v == 1 {
            return byte(i + 'a')
        }
    }
    return 0
}