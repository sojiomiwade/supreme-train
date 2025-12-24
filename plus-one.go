/*
9
n, m: 2 1
ans [0 0]
*/
func plusOne(digits []int) []int {
    n := 1 + len(digits)
    m := len(digits)
    for _,v := range digits {
        if v != 9 {
            n --
            break
        } 
    }
    c, ans := 1, make([]int, n)
    for i := m - 1; i >= 0; i -- {
        ans[i+(n-m)] = (digits[i] + c) % 10
        c = (digits[i] + c) / 10
    }
    if n == 1 + m {ans[0] = 1}
    return ans
}