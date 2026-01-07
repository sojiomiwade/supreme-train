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
// memo: d5 = d4 + d3

func climbStairs(n int) int {
    if n == 1 { return 1 }
    d := make([]int, n + 1)
    d[1],d[2] = 1, 2
    var cs func(int) int

    cs = func (n int) int {
        if d[n] != 0 { return d[n]}
        d[n] = cs(n-1) + cs(n-2)
        return d[n]
    }
    return cs(n)
}