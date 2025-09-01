/*
n**2: loop on both indices and check if ni and nj sum to target. 
n: 
2 11 7 15
target = 9
  ^
l = {2:0, 11:1, }
[t-nums[i]] in l.keys? if so? return i, l[t-nums[i]]

2 11 7 15
     i
l = {2:0, 11:1, }
res = []int{2,0}
*/
func twoSum(nums []int, target int) []int {
    l := make(map[int]int)
    for i, val := range nums {
        if oi, ok := l[target - nums[i]]; ok {
            return []int{i, oi}
        }
        l[val] = i
    }
    return []int{}
}

// func twoSum(nums []int, target int) []int {
//     for i := range len(nums) {
//         for j := range i {
//             if nums[i] + nums[j] == target {
//                 return []int{i,j}
//             }
//         }
//     }
//     return []int{}
// }
