/*
remove spaces from back
then count from first char until space or start of string
" joy  "
    f
  l

"joy"
 l f

 "j"
  f
  l

"d a  "
   r
  l
*/
func lengthOfLastWord(s string) int {
    n := len(s)
    var l, r int
    for r = n - 1; r >= 0; r -- {
        if s[r] != ' ' {
            break
        }
    }
    for l = r; l >= 0; l -- {
        if s[l] == ' ' {
            break
        }
    } 
    return r - l 
}