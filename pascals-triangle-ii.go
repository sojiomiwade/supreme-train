// 1
// 1 1
// 1 2 1
// 1 3 3 1
// 1 4 6 4 1

// ai =  
// make an array and repeatedly perform ai = ai + ai-1 --- i in [1,rowIndex] for r in [0,rowIndex]
// init conds for each row a0 = a_rowindex = 1

// rowIndex 2
// r 2
// ans [1 3 1 1]
//        i
// ans  1 3 3 1
//      i
// last 1 2 1 0
// r 2

func getRow(rowIndex int) []int {
    ans := make([]int, 1 + rowIndex)
    last := make([]int, 1 + rowIndex)
    ans[0] = 1
    last[0] = 1
    for r := range rowIndex + 1 {
        ans[r] = 1
        for i := 1; i < r; i ++ {
            ans[i] = last[i] + last[i - 1]
        }
        for i := range (len(ans)) {
            last[i] = ans[i]
        }
    }
    return ans
}