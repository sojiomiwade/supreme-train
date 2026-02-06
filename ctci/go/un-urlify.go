package main

import "fmt"

/*
given a string with arbirary capacity, and a len,
un-urlify the string, return the new length too

in  : mr%20John%20Smith, 17
out : mr john smith, 13

mr%20John%20Smith
                r
            l
mr John Smith
writing from left on a[l] from a[r] to right ok
increment r by 3 if %20 is next set of chars; l always increments by 1

ab%20c...... slen = 6
      r
    l
ab c0c...... slen = 6

expect "ab c" byte array with len 4
*/

func unurlify(arr []byte, slen int) int {
	var l,r int
	for l,r = 0,0; r < slen; l ++ {
		if string(arr[r:r+3]) != "%20" {
			arr[l] = arr[r]
			r ++
		} else {
			arr[l] = ' '
			r += 3
		}
	}
	return l
}

func main() {
	arr := [50]byte{}
	s := "Mr%20John%20Smith" 
	copy(arr[:],[]byte(s))
	fmt.Println(s, len(s), len(arr)) // s, 17, 50
	sarr := arr[:]
	newlen := unurlify(sarr, len(s))
	fmt.Printf("%q,%d\n",string(arr[:newlen]),newlen) // "'Mr John Smith', 13"

	s = "Mr%20John%20Smith%20"
	copy(arr[:],[]byte(s))
	fmt.Println(s, len(s), len(arr)) // s, 20, 50
	newlen = unurlify(arr[:], len(s))
	fmt.Printf("%q,%d\n",string(arr[:newlen]),newlen) // "'Mr John Smith ', 14"
}