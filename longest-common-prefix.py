/*
flower
flow
flight

--
""
--
loop j forever
    loop i on 1..m
        if j is outside of bound of any string OR doesn't match strs[i][j] and strs[i-1][j]
            return strs[0][0..j]

return strs[0]

lebcowit
complexity: mn -- m number of strings, n is length of longest string

fl
f
ans --> f
i,j: 21
st,s: fl, f


---
""
---
*/
func longestCommonPrefix(strs []string) string {
    for j := 0; j<len(strs[0]); j++ {
        for i := 1; i < len(strs); i ++ {
            st,s:=strs[i-1],strs[i]
            if j>=len(st) || j>=len(s) || st[j]!=s[j] {
                return s[:j]
            }
        }
    }
    return strs[0]
}
