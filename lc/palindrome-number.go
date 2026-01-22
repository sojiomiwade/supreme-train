/*
121 3443 -- examples
app 1: turn it into a string and see if the reverse is the same as it
app 2: 
- make the reverse into 1 digit at a time -- more thinking
- -ve => not palindrome
1 2 1
  i   
  j


*/
func isPalindrome(x int) bool {
    xx := strconv.Itoa(x)
    for i,j := 0,len(xx)-1; i<j; i,j=i+1,j-1 {
        if xx[i] != xx[j] { return false}
    }
    return true
}
