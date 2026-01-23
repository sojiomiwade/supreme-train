/*
URLify: Write a method to replace all spaces in a string with ‘%20’. You may assume that the string has sufficient space at the end to hold the additional characters and that you are given the true length of the string.

Example:
Input : Mr john Smith

Output: Mr%20john%20Smith...

0123456789
  smith john
        t
        b
smith%20
0123456789
Mr john Smith
      t
		b
     %20Smith \n
get the new length: n
then start from n and go back down to 0
if not a space put it. 
if space, then put 0 2 and % in the three holes (j, j-1, j-2, resp.)
*/
package main

import "fmt"

/*
arr:
012345678
ab c
 t
 b
ab%20c 
012345678

m = 4
scount 1
n = 4 + 2*1 = 6
expect: "ab%20 c"
3 spaces %20 3 times --> total extra 2 * 3
*/
func urlify(arr []byte, m int) int {
	scount := 0
	for i := range m {
		if arr[i] == ' ' {
			scount ++
		}
	}
	n := m + scount * 2

	b := n - 1
	for t := m - 1; t >= 0; t-- {
		if arr[t] != ' ' {
			arr[b] = arr[t]
			b --
		} else {
			arr[b] = '0'
			arr[b-1] = '2'
			arr[b-2] = '%'
			b -= 3
		}
	}
	if b != -1 {
		panic(b)
	} 
	return n
}

func main() {
	ba := [50]byte {} // byte array with long enough length
	s := "ab cdef ghijk"
	for i,ch := range s {
		ba[i] = byte(ch) 
	}
	fmt.Println(ba)
	fmt.Println([]byte("%20"))
	// fmt.Println([]rune("%20"))
	n := urlify(ba[:], len(s))
	fmt.Println(string(ba[:n]))
}
