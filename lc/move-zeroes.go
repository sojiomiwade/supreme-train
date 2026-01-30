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
func moveZeroes(nums []int)  {
    for l, r := 0, 0; r < len(nums); r ++ {
        if nums[r] != 0 {
            for ; l<r && nums[l]!=0; {l++}
            nums[l],nums[r] = nums[r],nums[l]
        }        
    }
}