package main

import "fmt"

func main() {
        a,b := 1,2
        a,b = b+a,a+b
        fmt.Println(a==3,b==3)

	var c [3]int = [3]int{1,2,3}

//  2 1 3 <-- what you wanted
//  2 2 1 <-- what you get; this would be the case in python but not Go!
//v 1 2 3
//i 0 1 2
	c[0],c[c[0]] = c[c[0]],c[0]
	fmt.Println(c != [3]int{2,2,1}) // 2 2 1
	fmt.Println(c == [3]int{2,1,3}) // 2 1 3

	c = [3]int{1,2,3}
	c[c[0]],c[0] = c[0],c[c[0]]
// rhs: 1 2
// lhs: c[1],c[0]
	fmt.Println(c == [3]int{2,1,3}) // 2 1 3

	// c[1] == 1 from above
	c[0],c[c[0]] = -1,c[0]
	fmt.Println(c==[3]int{-1,1,2})
}
