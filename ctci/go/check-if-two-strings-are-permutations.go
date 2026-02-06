package main


import "fmt"


// check if two given strings are permutations of each other


/*
s: h e l l o b o y


t: l l o h e b y o


freq[h0 e0 l0 o0 b0 y0] -- true


sort both and check 1 char at a time: time,space: O(n lg n), O(n)
freq array -- freq[ch] goes up and down, if ch is in s or t respectively
return true if all is zero in the array. otherwise, return false


either way: can return false immediately if len is not the same


a b a
b a a
freq [a0 b0]
*/
func checkperm(s, t string) bool {
   freq := [256]byte{}
   slen, tlen := len(s), len(t)
   if slen != tlen {
       return false
   }
   for i := range slen {
       freq[s[i]]++
       freq[t[i]]--
   }
   for _, val := range freq {
       if val != 0 {
           return false
       }
   }
   return true
}


func main() {
   s, t := "hello", "llohe" // true
   fmt.Println(true == checkperm(s, t))


   s, t = "", "" // true
   fmt.Println(true == checkperm(s, t))


   s, t = "12345", "12345" // true
   fmt.Println(true == checkperm(s, t))


   s, t = "123", "231" // true
   fmt.Println(true == checkperm(s, t))


   s, t = "123", "1" // false
   fmt.Println(false == checkperm(s, t))


   s, t = "dsfl90sufjsiojfni", "sdfsofhosij" // false
   fmt.Println(false == checkperm(s, t))


   // indexes of an array can be int, byte or rune!
   shoe := [5]rune{}
   var r rune = 1
   var c byte = 2
   var i int = 3
   shoe[r] = 4
   shoe[c] = 5
   shoe[i] = 6
   fmt.Println(shoe)


   for i, rv := range s {
       fmt.Printf("%T---%T\n",s[i], rv)
   }
   // pretty sure s[i] of a string type is byte! NO IT IS actually rune!!!
   fmt.Printf("%T %T\n", shoe[0], s) // byte or uint8, string


   // no problem is too small or too easy
   // when something doesn't go right, use bisection (or linearity if you have that time from the beginning of the code) to find out what went wrong
}




