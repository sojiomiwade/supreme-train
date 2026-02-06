// i         j
// A   m a q , a 
// 0 1 2 3 4 5 6
//     l
//         r
// sl sr a a 
// implmenet a revert but always continue until 
// 
func isPalindrome(s string) bool {
    for l, r := 0, len(s) - 1; l < r; {
        sl, sr := s[l], s[r]
        if ('A' <= sl && sl <= 'Z') { sl += ('a'-'A')}
        if ('A' <= sr && sr <= 'Z') { sr += ('a'-'A')}
        if ! (('a' <= sl && sl <= 'z') || ('0' <= sl && sl <= '9') ) { 
            l++
            continue
        }
        if ! (('a' <= sr && sr <= 'z') || ('0' <= sr && sr <= '9')) { 
            r--
            continue
        }
        if l > r || sl != sr { return false }
        l, r = l + 1, r - 1
    }
    return true
}