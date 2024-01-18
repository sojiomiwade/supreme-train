'''
serialize and deserialize BST
            5
        3       8
      n   4        9
53489

deser_bst(que,lb,ub)
    if not lb<que[0]<ub:
        return None
    x=que.popleft
    root=node(x)
    root.left=deser_bst(que,lb,x)
    root.right=deser_bst(que,x,ub)
    return root

deser_bst(que,-inf,inf)
'''