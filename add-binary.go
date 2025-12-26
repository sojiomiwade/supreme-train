/**
 11
  1
100

c t b .. 
if count > 1 then c = 1, else c = 0
if count % 2 == 1, then s = 1. else s is 0
when all done, if c is 1, then pad 1 in front of ans

ensure a is the bigger one for simplicity
first ensure a and b are same length
a 5, b 2 --> pad len(a)-len(b) 0s to the left of b

read from right to left to get ai, bi
complexity: m + n
1010
1011
a 11
b 01
m, n, i 2 1 0
carry "1"
ans [0 0]
count 1 + 1 + 0 = 2
s 0

11 01 100
a b m n: 11 01 2 2 
buf: ""
ans: 1 + ['0' '0']
i 0
count = 1 + 1 + 0 = 2
carry: '1'

**/
func addBinary(a string, b string) string {
    m, n := len(a), len(b)
    if m < n {
        a, b = b, a
        m, n = n, m
    }
    buf := ""
    for i := 0; i < m-n; i++ {
        buf += "0"
    }
    b = buf + b
    var carry byte = '0'
    ans := make([]byte, m)
    for i := m - 1; i >= 0; i-- {
        count := carry - '0' + byte(a[i]) - '0' + byte(b[i]) - '0'
        carry = '0'
        if count > 1 { carry = '1' }
        ans[i] = '0'
        if count % 2 == 1 { ans[i] = '1' }
    }   

    if carry == '1' { return "1" + string(ans[:]) }
    return string(ans[:])

}