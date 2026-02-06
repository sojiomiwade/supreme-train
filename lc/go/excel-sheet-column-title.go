// a 1
// b 2
// c 3
// ...
// z 26
// aa 27 = a * 26 + a
// ab 28 = b * 26**0 + a * 26 = 28
// zy ?? = y * 26**0 + z * 26 = 25 + 26 * 26**1 = 701

// 1 a
// 2 b
// 26 z
// 28 = 1 + '2' = ab
// 701 % 26 = 25 -- 
// 701 / 26 = 26 -- 
// 26 % 26 = 0 + 1 --> a

// read the question!

// code: for each char from the back

// 1 % 26 = 1    - 1 + 'A' = A
// 2 % 26 = 2    - 1 + 'A' = B
// 25 % 26 = 25 
// 26 % 26 = 0 - 1 %26 + 'A' = Z

// keep moding and -1: (val - 1) + 'A'
// keep diving until you get 0 ---

// c 1
// buf [BA]
// val 2
// zz = 26 + 26*26
// 0 --> 26
// 1 + 26 = 27
// 701 -- 
// 26 -- 0 + 26 * 25
// 701 -- y
func convertToTitle(columnNumber int) string {
    buf := []byte{}
    for c := columnNumber; c != 0; {
        c -= 1
        ch := 'A' + byte(c % 26)
        buf = append(buf, ch)
        c /= 26
    }
    for l,r := 0,len(buf)-1; l<r; l,r = l+1,r-1 {
        buf[l],buf[r] = buf[r],buf[l]
    }
    return string(buf)
}