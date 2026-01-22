// frequency map
// f {3:2, 2:1}

// 3 2 3
// f {3:2, 2:1}
// fmax, ans 2 3

func majorityElement(nums []int) int {
    f := map[int]int{}
    fmax, ans := 0, 0
    for _,v := range nums {
        f[v] ++
        if f[v] > fmax {
            fmax, ans = f[v], v
        }
    }
    return ans
}