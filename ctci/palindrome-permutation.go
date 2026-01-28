package main

import "fmt"
import "unicode"

/*
count twins, convert case and ignore space
can use bool array. expect all should be 
false at end, except 1 or 0.
*/


func ispp(s string) bool {
  a := [26]bool {}
  for _,ch := range s {
    if !unicode.IsLetter(ch) { continue }
    v := unicode.ToLower(ch) - 'a'
    a[v] = !a[v]
  }

  set := false
  for _,av := range a {
    if av {
      if set { return false }
      set = true
    }
  }   
  return true
}

func main() {
  // all letters have twins
  in := "tactca" 
  fmt.Println(ispp(in) == true)

  // no more than one letter (exactly 1 
  // in this example) may have no twin
  in = "tactcoa" 
  fmt.Println(ispp(in) == true)

  // 1 space
  in = "Tact Coa"
  fmt.Println(ispp(in) == true)

  // multiple spaces
  in = "Tact    coa"
  fmt.Println(ispp(in) == true)

  // ditto 
  in = "x "
  fmt.Println(ispp(in) == true)

  // ditto 
  in = ""
  fmt.Println(ispp(in) == true)

  // two letters don't have twins
  in = "tactco"
  fmt.Println(ispp(in) == false)

  // ditto 
  in = "co"
  fmt.Println(ispp(in) == false)
}
