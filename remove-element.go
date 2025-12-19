/*
  5 4 3 2 
 
      a
        b
a starts at -1
if nums[b]!=val, then increment a, and overwrite what is at a
return a + 1

corner: 
0 elements --> 0 OK
1 element --> 0 or 1 OK
 
 323
 223
 a
   b
*/
func removeElement(nums []int, val int) int {
    a := -1
    for _, valb := range(nums) {
        if valb != val {
            a++
            nums[a] = valb
        }
    }
    return a + 1   
}