package main

import "fmt"

/*
*ale
j
 i
pale


noon
i
noo*

if strings different length, 
  if first chars not the same, advance the bigger string iterator by one char and set c = 1
  
same length is easy, count can be boolean by the way.


if strings are different lengths, add a wildcard
if one char less, then adding to the front
or back
pales
    i
pale

ensure s is always less or equal to t
if less
ple
pale
set edit and advance bigger

*/

func oa(s, t string) bool {
	slen,tlen := len(s),len(t)
	if slen > tlen {
		slen,tlen = tlen,slen
		s,t = t,s
	}
	if tlen > slen + 1 {
		return false
	}

	if slen == tlen {
		edit := false
		for i := 0; i < slen; i++ {
			if s[i] != t[i] {
				if edit {
					return false
				}
				edit = true
			}
		}
		return true
	}
	
	// s + 1 == t
	edit := false
	for i,j:=0,0; j<tlen; j++{
		if i==slen || s[i] != t[j] {
			if edit {
				return false
			}	
			edit = true		
		} else {
			i++
		}	
	}
	return true
}

func main() {
	s, t := "pale", "ple"
	fmt.Println(oa(s,t)==true)

	s, t = "pales", "pale"
	fmt.Println(oa(s,t)==true)

	s, t = "pale", "bale"
	fmt.Println(oa(s,t)==true)

	s, t = "pale", "pa"
	fmt.Println(oa(s,t)==false)

	s, t = "", ""
	fmt.Println(oa(s,t)==true)

	s, t = "pale", "bake"
	fmt.Println(oa(s,t)==false)

	s, t = "pale", "ale"
	fmt.Println(oa(s,t)==true)

}
