/** 
 * Forward declaration of isBadVersion API.
 * @param   version   your guess about first bad version
 * @return 	 	      true if current version is bad 
 *			          false if current version is good
 * func isBadVersion(version int) bool;
 */
// 1 2 3 4 5 6 7 8 9 
// g g b b b b b b b
//    r   r
// binsearch: if bad remember it, and bisect left
// if good, bisect right
// brute force: iterate through linearly till you find the first bad. O(n) time, O(1) space
// there is 
//   1   2   3
//   b   b   b
// h lm  
// a = 1
func firstBadVersion(n int) int {
    lo, hi := 1, n
    ans := -1
    for ; lo <= hi; {
        mi := lo + (hi - lo) / 2
        if isBadVersion(mi) {
            ans = mi
            hi = mi - 1
        } else {
            lo = mi + 1
        }
    }
    return ans
}