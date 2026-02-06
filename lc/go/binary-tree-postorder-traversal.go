/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
//  ans: 4 2 3 1
// po (root)
//     po(left)
//     po(right)
//     process root

//           1
//         /   \
//        2     3
//         \   /
//          4 5
                     
// stval hprval 3f
// root x
// st  [1t]
// ans [4 2 5 3]
// exp [4 2 5 3 1]

// 2 stacks: hadpushedright, and st
// while st or root
//     if root
//         push (root, false) to stack
//         root = root.left
//     else:
//         stval, hprval = st.pop()
//         if not hprval:
//             st.append(stval, true)
//             root = stval.right
//         else: 
//             process(stval)
//         1 
//       2    3 
// expect: 2 3 1
// root  3      
// st [1t]
// stval 1f
// ans [2]

type pair struct {
    node *TreeNode
    rightdone bool
}
func postorderTraversal(root *TreeNode) []int {
    ans := []int{}
    for st := []pair{}; root != nil || len(st) > 0; {
        if root != nil {
            st = append(st, pair{root, false})
            root = root.Left
        } else {
            stval := st[len(st)-1]
            st = st[:len(st)-1]
            if !stval.rightdone {
                st = append(st, pair{stval.node, true})
                root = stval.node.Right
            } else {
                ans = append(ans, stval.node.Val)
            }
        }
    }
    return ans
}
