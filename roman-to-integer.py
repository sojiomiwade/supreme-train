/***
iii 3
lviii 50 
if no i, no deductions
i iv ix
xl xc
cd cm
ixc require looking forward

1st pass
just add everything

2nd pass
iv/ix -- remove 2; 
xl/xc -- remove 20
cd/cm -- remove 200

liv
***/
func romanToInt(s string) int {
   s = strings.ToLower(s)
   ans := 0
   for i,c := range s {
    switch c {
        case 'i': ans += 1
        case 'v': ans += 5
        case 'x': ans += 10
        case 'l': ans += 50
        case 'c': ans += 100
        case 'd': ans += 500
        case 'm': ans += 1000
    }
    if i!=len(s)-1 {
        switch s[i:i+2] {
            case "iv","ix" : ans -= 2
            case "xl","xc": ans -= 20
            case "cd","cm": ans -= 200 
        }
    }
   }
   return ans
}
