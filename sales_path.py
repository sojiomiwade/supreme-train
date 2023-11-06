'''
Sales Path
The car manufacturer Honda holds their distribution system in the form of a tree (not necessarily binary). The root is the company itself, and every node in the tree represents a car distributor that receives cars from the parent node and ships them to its children nodes. The leaf nodes are car dealerships that sell cars direct to consumers. In addition, every node holds an integer that is the cost of shipping a car to it.

Take for example the tree below:
                           0
                        /  |  \
                      /    |    \
                     5     3      6
                    /    /  \    /  \ 
                   4    2    0  1    5
                       /    /
                      1    10
                       \
                        1
func mincost(node)
    return node.cost + mincost amongs each child
A path from Honda’s factory to a car dealership, which is a path from the root to a leaf in the tree, is called a Sales Path. The cost of a Sales Path is the sum of the costs for every node in the path. For example, in the tree above one Sales Path is 0→3→0→10, and its cost is 13 (0+3+0+10).

Honda wishes to find the minimal Sales Path cost in its distribution tree. Given a node rootNode, write a function getCheapestCost that calculates the minimal Sales Path cost in the tree.

Implement your function in the most efficient manner and analyze its time and space complexities.

For example:

Given the rootNode of the tree in diagram above

Your function would return:

7 since it’s the minimal Sales Path cost (there are actually two Sales Paths in the tree whose cost is 7: 0→6→1 and 0→3→2→1→1)

Constraints:

[time limit] 5000ms

[input] Node rootNode

0 ≤ rootNode.cost ≤ 100000
[output] integer

                           0
                        /  |  \
                      /    |    \
                     5     3      6
                    /    /  \    /  \ 
                   4    2    0  1    5
                       /    /
                      1    10
                       \
                        1

gcc(6)
    gcc(1)

    gcc(5)
'''
from __future__ import annotations
from typing import List, Optional

class TreeNode:
    MAX_COST = 0

    def __init__(
            self, cost: int, 
            children_costs: Optional[List[int]] = None,
            ) -> None:
        TreeNode.MAX_COST = max(TreeNode.MAX_COST, cost)

        self.cost = cost
        if children_costs:
            self.children = \
            [TreeNode(childcost) for childcost in children_costs]
        else:
            self.children = None

def get_cheapest_cost(rootNode: TreeNode) -> int:
    if not rootNode:
        raise ValueError('no root node')
    if not rootNode.children:
        return rootNode.cost

    min_child_cost = TreeNode.MAX_COST
    for node in rootNode.children:
        min_child_cost = min(min_child_cost, get_cheapest_cost(node))
    return rootNode.cost + min_child_cost

print(get_cheapest_cost(TreeNode(6, [1,5]))) # 7