// 4 5 1 3 0 0 0
//         l
//           r
// 4 5 1 3 0 0 0
// l
//     r

// l must always sit on a 0
// r finds nonzeroes till it reaches the end

// 4
// l
// r
//
// 5 0 9 3
// 5 9 0 3
//   l
//       r
// loop on r
//     if r on nonzero
//         move l to first zero less than or equal to r, or itself
//         swap them
// 4 5 1 3 0 0 0 <-- expected
// 0 0 4 5
// 4 5 4 5
//     l
//       i
func moveZeroes(nums []int)  {
    l := 0
    for i := 0; i < len(nums); i ++ {
        if nums[i] != 0 {
            nums[l] = nums[i]
            l++
        }        
    }
    for i := l; i < len(nums); i ++ {
        nums[i] = 0
    }
}