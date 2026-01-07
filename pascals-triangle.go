// 1 1
// 2 1 1
// 3 1 2 1
// 4 1 3 3 1
// 5 1 4 6 4 1

// ans[0] = [1]
// repeat i = 1...n-1 inclusive times
//     p = ans[i-1]
//     create slice a that is i+1 long
//     set a[0] = a[i] = 1
//     then for j = 1...i-1: a[j] = p[j] + p[j-1]
//     ans[i] = a

// n = 3
// ans = [[1], [1,1], []]
//                p
// i 2
// a [1 2 1]
// p
func generate(n int) [][]int {
    ans := [][]int{}
    ans = append(ans, []int{1})
    for i:=1; i<n; i++ {
        p := ans[i-1]
        a := make([]int,i+1)
        a[0],a[i] = 1,1
        for j := 1; j < i; j++ {
            a[j] = p[j] + p[j-1]
        }
        ans = append(ans, a)
    }
    return ans
}