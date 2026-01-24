package main

import (
	"cmp"
	"fmt"
	"slices"
	"sort"
)

func SojiPrint(a []int, f func() int) {
	fmt.Println("hi", a[0], f())
}

func main() {
	na := []int{2, 3}
	var i int
	myf := func() int { return na[i] }

	SojiPrint(na, myf) // prints 2 2
	nb := []int{1}

	// prints 1 2
	// the anonymous function myf closed over the name na in its definition
	// not the slice the name refers too.
	// so if na refers to another slice, the function my goes with the new slice
	SojiPrint(nb, myf)

	// example 2a
	aa := make([]byte, 10)
	shoe := func(i, j int) bool { return aa[i] < aa[j] }
	ba := []byte{'a', 1, '3', 3}
	sort.Slice(ba, shoe)
	fmt.Println("example 2a", ba) // should not be sorted per argument above

	// example 2b: only change is we have only one slice ref, not two
	ba = make([]byte, 10)
	shoe = func(i, j int) bool { return ba[i] < ba[j] }
	ba = []byte{'a', 1, '3', 3}
	sort.Slice(ba, shoe)
	fmt.Println("example 2b", ba) // should *be* sorted per argument above

	// not applicable, stuff above has to do with a
	// name used in the anon function but is
	// outside the anon function definition
	negcomp := func(a, b byte) int {
		return -cmp.Compare(a, b)
	}
	slices.SortFunc(ba, negcomp)
	fmt.Println("example 3 (n/a)", ba)
}
