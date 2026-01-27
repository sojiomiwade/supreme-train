/*
sort then find the missing one: O(n lg n) and O(n) time and space
place all [0,n] elements in a set, then remove till one left: O(n) and O(n)

2 4 6 5 3 0
2 4 1 5 0 | 3 <-- missing
0 1 2 5 4
0 1 2 3 4   5

2 4 6 5 3 0
6 
0 1 2 3 4 5




1 8 1 8 2 3 2 

xor sum,

regular sum

confidence

the missing element: the one not in its place or its n!
approach: iterate through the n elements; for each element, stay on that place
and keep swapping elements into their place
O(n) and O(1)
nums: [0 2]
all {1}
0 2

0 

0 1   3 4 5   | 0 1 2 3 4
0 1 2 3 4 5

3 0 1
0 1 2 3
*/
func missingNumber(nums []int) int {
    n := len(nums)
    ans := 0
    for i := range n {
        ans ^= i ^ nums[i]
    }
    return ans ^ n

    // n := len(nums)
    // sum := n * (n + 1) / 2 
    // for _, v := range nums {
    //     sum -= v
    // }
    // return sum
    // nlen := len(nums)
    // for i, _ := range nums {
    //     for ; i != nums[i] && nums[i] != nlen; {
    //         v := nums[i]
    //         nums[i], nums[v] = nums[v], nums[i]
    //     }
    // }
    // for i,v := range nums {
    //     if v == nlen {
    //         return i
    //     }
    // }
    // return nlen


    // all := map[int]struct{} {}
    // for i := range 1 + len(nums) {
    //     all[i] = struct{} {}
    // }
    // for _, v := range nums {
    //     if _, ok := all[v]; ok {
    //         delete(all, v)
    //     }
    // }
    // var ans int
    // for k := range all {
    //     ans = k
    //     break
    // }
    // return ans
}