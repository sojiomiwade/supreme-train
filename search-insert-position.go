/*
1 3 5 6
a b c d          
a 1  

2, 3-->1
lo mi hi 0 0 0
*/
func searchInsert(nums []int, target int) int {
    n := len(nums)
    lo, hi := 0, n - 1
    for ; lo <= hi; {
        mi := lo + (hi - lo) / 2
        if nums[mi] == target { return mi }
        if nums[mi] < target { 
            lo = mi + 1
        } else {
            hi = mi - 1
        }
    } 

    return lo
}