#Link to problem: https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#Time complexity: O(n)
#Space complexity: O(n)
                        
from collections import deque
from typing import Optional
from help.treeNodeDefinition import TreeNode
from help.seed_binary_tree import seed_binary_tree, print_binary_tree
                       
class Solution:
    def binary_tree_level_order_traversal(self,root:Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []
        queue = deque()
        res = []
        
        queue.append(root)
        curr_level = 0
        while queue:
            
            n = len(queue)
            res.append([])
            for _ in range(n):
                node = queue.popleft()
                res[curr_level].append(node.val)
                
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            curr_level += 1
        
        return res
                                        
solution = Solution()
head = seed_binary_tree()
head_after = solution.binary_tree_level_order_traversal(head)
print_binary_tree(head_after)
    
head = seed_binary_tree()
head_after = solution.binary_tree_level_order_traversal(head)
print_binary_tree(head_after)
