/*
sort then find the missing one: O(n lg n) and O(n) time and space
place all [0,n] elements in a set, then remove till one left

2 4 6 5 3 0
2 4 1 5 0 | 3 <-- missing
0 1 2 5 4
0 1 2 3 4   5

2 4 6 5 3 0
6 
0 1 2 3 4 5

confidence

the missing element: the one not in its place or its n!
approach: iterate through the n elements; for each element, stay on that place
and keep swapping elements into their place

nums: [0 2]
all {1}
*/
func missingNumber(nums []int) int {
    all := map[int]struct{} {}
    for i := range 1 + len(nums) {
        all[i] = struct{} {}
    }
    for _, v := range nums {
        if _, ok := all[v]; ok {
            delete(all, v)
        }
    }
    for k := range all {
        return k
    }
    return -1
}