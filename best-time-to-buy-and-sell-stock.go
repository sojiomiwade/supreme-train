// 7 1 5 3 6 4 0 7
//   .     .
// 0 1 2 3 4 5 6 7
// 0 0 4 2 5 3 0 7
// change minbound only if you find something lower
// maxprofit is always max(maxprofit, curr - minbound)
// minbound 1
// maxprofit 4 
// corner case: with one day, prof is zero --> init maxprofit to 0
// works for mono decreasing too to give zero
// 1 5 3 -- exp 4
//     c
// minbound 1
// maxprofit 4
func maxProfit(prices []int) int {
    maxprofit, minbound := 0, prices[0]
    for _, curr := range prices {
        minbound = min(minbound, curr)
        maxprofit = max(maxprofit, curr - minbound)
    }
    return maxprofit
}