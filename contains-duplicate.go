/*
1 2 3 1
      ^ 
set: call it seen {1 2 3} -- set O(n) time and space
sort: space can be O(1), and time O(n lg n)
1 2 3 1 -- true
1 2 3 -- false
*/
func containsDuplicate(nums []int) bool {
    seen := map[int]struct{} {}
    for _, el := range nums {
        if _, ok := seen[el]; ok {
            return true
        }
        seen[el] = struct{}{}
    }
    return false
}