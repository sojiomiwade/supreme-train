// 1 2 3 0 0 0, 2 5 6
// 1 2 3 0 0 0

// 1 2 3 0 0 0
//       i
// j
// 5 6 7

// 1 3 5 0 0 0
//   i
// j
// 2 4 6

// ans: 1 2 3 4 5 6

// start with new array equal m. which has copy of n1's m values'
// then merge new and n2 into n1
// if n2 has smaller swap it with n1 val.
// i always moves

// n1 1 2 3 4
// n2 2 4
//        j
//        i
// nn 1 3
func merge(n1 []int, m int, n2 []int, n int)  {
    nn := make([]int, m)
    for i := range m {
        nn[i] = n1[i]
    }
    
    for i,j := 0,0; i < m || j < n; {
        nnval, n2val := 1 + 1000000000, 1 + 1000000000
        if i < m {nnval = nn[i]}
        if j < n {n2val = n2[j]}
        if nnval < n2val {
            n1[i+j] = nn[i]
            i ++
        } else {
            n1[i+j] = n2[j]
            j ++
        }
    }
}