// 1 = 1^2 = 1

// 4 5 3 4 ... stop -- not happy
// 8 9 ... 1 ... happy
// 1 
// need a hashset to know if we saw the number before...
// 2 = 4
// 4 -- 16
// 1 6 -- 37
// 3 7 -- 9 + 49 = 58
// 5 8 -- 25 + 64 = 89
// 8 9 -- 72 + 81 = 159

type nothing struct{}
func isHappy(n int) bool {
    seen := map[int]nothing {}
    for ; n != 1; {
        sum := 0
        for ; n != 0; {
            sum += (n % 10) * (n % 10)
            n /= 10
        }
        if _, ok := seen[sum]; ok { return false }
        seen[sum] = nothing{}
        n = sum

    }
    return true
}