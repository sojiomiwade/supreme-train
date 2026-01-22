/*
0,1,1,1,1,2,2,3,3,4
a   
          b
compare b to a: if different, put nums[b] into nums[a+1]; a++
ans: a+2

corner: if len is 1 just return 0
0
a
  b
return 

5 5-8 8
  a
      b
*/
func removeDuplicates(nums []int) int {
    n := len(nums)
    a, b := 0, 1   
    for ; b < n; b ++ {
        if nums[b] != nums[a] {
            a++
            nums[a] = nums[b]
        }
    }
    return a + 1
}