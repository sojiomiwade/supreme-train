func isUgly(n int) bool {
    if n < 1 {
        return false
    }
    for _,p := range []int {2,3,5} {
        for ; n % p == 0; {
            n /= p
        }
    }
    return n == 1

}