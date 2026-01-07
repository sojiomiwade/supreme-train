// 2
// 1 1
// 2

// 1 1 1
// 1 2
// 2 1

// c(5) = 
// c1 = 1
// c0 = 0
// c2 = 2
// c3 = c2 + c1 = 3
// c4 = c3 + c2
func climbStairs(n int) int {
    if n == 1 { return 1 }
    if n == 2 { return 2 }
    a, b := 1, 2
    for i := 3; i <= n; i ++ {
        b, a = b + a, b
    }
    return b
}