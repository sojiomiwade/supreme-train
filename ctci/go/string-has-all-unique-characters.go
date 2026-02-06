package main


import (
   "fmt"
   "slices"
)


/**
Implement a function to check if a string has all unique characters


**/


/*
could use a set. time: O(n). space: O(n)
could sort a slice: time: O(n lg n). space: O(n)


aba
^
have {a, b}
ch a


ab
*/


func unique_chars(s string) bool {
   t := []rune(s)
   comp := func(a, b rune) int {
       return int(a - b)
   }
   slices.SortFunc(t, comp)


   // fmt.Println(t)
   for i := range len(t) - 1 {
       if t[i] == t[i+1] {
           return false
       }
   }
   return true
   // have := map[rune]struct{} {}
   // for _, ch := range s {
   //  if _, ok := have[ch]; ok {
   //      return false
   //  }
   //  have[ch] = struct{}{}
   // }
   // return true
}


func main() {
   s := ""
   fmt.Println(unique_chars(s)) // true


   s = "abcde1234ABCDE"
   fmt.Println(unique_chars(s)) // true


   s = "O0#*"
   fmt.Println(unique_chars(s)) // true


   s = "aa"                     // only duplicates
   fmt.Println(unique_chars(s)) // false


   s = "fee"                    // duplicates at the end
   fmt.Println(unique_chars(s)) // false


   s = "12345678osjfjsdfh sahnks fdfsdfas. sdfasf ssdf faf aasdf fasfasfas" // big string
   fmt.Println(unique_chars(s))                                             // false
}






