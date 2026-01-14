/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
//   9 9 9 3 2 6 4 1 8 4 5
//         i
//         j       
//   3 5 6 1 8 4 5

// 1. reverse the two lists!
// 2. then find *last* common node
// 3. then reverse both lists back!
// 4. return last
// complexity: same as before but space is constant now!

// sweep through headA and keep all in a hashmap
// then sweep through headB until you find something in the map... thats your answer!
// time: O(m + n)
// space: O(min(m,n))
// heada 1 2 3
// headb 2 3

// have = {1n 2n 3n}

type nothing struct {}
func getIntersectionNode(headA, headB *ListNode) *ListNode {
    have := map[*ListNode]nothing {}
    for a := headA; a != nil; a = a.Next {
        have[a] = nothing{}
    }
    for b := headB; b != nil; b = b.Next {
        if _, ok := have[b]; ok { 
            return b 
        }
    }
    return nil
}