// n = 1 0 1 1
// 11 % 2 = 1
// 5 % 2 = 1
// 2 % 2 = 0
// 1 % 2 = 1
// 0 % wait we are done
// ans := 0; increment ans only if the % yields 1

// 1 1 0 
// ans 2
// n 0

func hammingWeight(n int) int {
    ans := 0
    for ; n != 0; {
        ans += n % 2
        n /= 2
    }
    return ans
}