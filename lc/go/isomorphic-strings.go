// a b c d e f g
// 0 1 2 3 4 5 6
//     fft
// egg  466 
// add  033
// mval 433
// sol: hashmap -- mapval ---mapval
//          f f f t t
// foo  --  5 o d o 5
// bar  --  b o g o q <--- not b!
// mval --  2 o g o 2

// key: s letters are the key, t values are the val

// loop through s: if sch is not yet there, put it in
//                 otherwise: check if mval[sru] == tru.
//                 if it is *not*: return false
// at end of func return true

// s 5 o 5
// t b o g
//       i
// val ok: b t
// mval {5:b o:o }

// b a d c
// b a b a
func isIsomorphic(s string, t string) bool {
    mval := map[byte]byte {}
    taken := [256]bool {}
    for i := range len(s) {
        sch := s[i]
        if val, ok := mval[sch]; !ok {
            if taken[t[i]] {
                return false
            }
            mval[sch] = t[i]
            taken[t[i]] = true
        } else {
            if val != t[i] {
                return false
            }
        }
    }
    return true
}