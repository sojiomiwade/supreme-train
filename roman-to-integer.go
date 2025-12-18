/*
liv
^^
if i beats i+1, then add i. otherwise take i away
at end, add the val of last
*/
func romanToInt(s string) int {
    val := map[rune]int{
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    // liv --> 
    // ans -- 50 - 1 + 5 = 54 
    // i 2
    ans := 0
    for i := 0; i < len(s) - 1; i++ {
        if val[rune(s[i])] < val[rune(s[i+1])] {
            ans -= val[rune(s[i])] 
        } else {
            ans += val[rune(s[i])] 
        }
    }
    return ans + val[rune(s[len(s)-1])]

}