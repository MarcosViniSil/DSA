from .treeNodeDefinition import TreeNode

def seed_binary_tree(values:list[int]) -> TreeNode:
    if len(values) == 0:
        return None
    root = TreeNode(values[0])

    i = 1
    while i < len(values):
        if values[i] is None:
            i += 1
            continue
        insert_value(root,values[i])
        i += 1
    
    return root

def insert_value(root:TreeNode,value:int) -> TreeNode:
    if root is None:
        return TreeNode(value)

    if value < root.val:
        root.left = insert_value(root.left, value)
    else:
        root.right = insert_value(root.right, value)

    return root

def print_binary_tree(root:TreeNode) -> None:
    if root is None:
        return
    print(root.val, end=", ")
    print_binary_tree(root.left)
    print_binary_tree(root.right)

