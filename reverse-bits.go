// n   0 1 0 0 0 1 1

// ans 1 1 0 0 0 0 0

// do this 31 times
// v = n & 1 // v = 1 or 0
// ans =>> 1
// ans |= mask // mask is 2**31. applied only if v != 0
// n =>> 1

// n    0 0 0
// ans  1 1 0 
// v    0 0 1
// mask 1 0 0

// 0 0 0 0
// n 0 0 0 0
// a 0 1 0 0
// m 0 0 1 0
// 31 --> 3
// i = 0, 1,  2 
func reverseBits(n int) int {
    ans, mone := 0, 1 << 30
    n >>= 1
    for _ = range 30 {
        if n & 1 != 0 {
            ans |= mone
        }
        mone >>= 1
        n >>= 1
    }
    return ans
}