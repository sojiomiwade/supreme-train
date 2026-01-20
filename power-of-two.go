/*
16 -- 10000 -- if there is only one 1, then it is a power of two
 110000
  01111
  0 ==> power of two
1
0 --> 0 
10
01
  00000
& 11111

0 1 0 1 1
      ^

1 1 0 1 1

only +ve included, then see if we get more than one modulo
another one: only +ve included, shift to see if we get more than 1 1

if n == 1 -- return true
if n is odd, -ve, 0 -- return false
otherwise: return isp(n/2)

n 4
n 0 0 0 1

9 --> log 
floor of log(9) != log(9)
but it would be for powers of 2 
*/
func isPowerOfTwo(n int) bool {
    if n <= 0 {
        return false
    }
    lg := math.Log2(float64(n))
    return math.Floor(lg) == math.Ceil(lg)



    // if n == 1 {
    //     return true
    // }

    // if n % 2 == 1 || n <= 0 {
    //     return false
    // }

    // return isPowerOfTwo(n >> 1)



    // if n <= 0 { 
    //     return false
    // }
    // alreadyhave := false
    // // n: 1
    // // n 011
    // // ah t
    // for ; n != 0; {
    //     if n % 2 == 1 {
    //         if alreadyhave {
    //             return false
    //         }
    //         alreadyhave = true
    //     }
    //     n >>= 1
    // }
    // return true



    // if n <= 0 {
    //     return false
    // }
    // s := strconv.FormatInt(int64(n), 2)
    // // fmt.Println(s, len(s))
    // have := false
    // for _, ch := range s {
    //     if ch == '1' {
    //         if have {
    //             return false
    //         }
    //         have = true
    //     }
    // }
    // return true


    // return n!=0 && n & (n-1) == 0
}