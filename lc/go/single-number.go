// 1 2 3 4 5 4 2 5 1 | 3
// 2 (1 2 4 5)

// 5 2 5 3 2
// 17 -- 3

// 0 1 0 1 
// 0 1 0 1

// xor them all!!!

func singleNumber(nums []int) int {
    ans := 0
    for _, x := range nums {
        ans ^= x
    }
    return ans
}