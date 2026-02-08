#Link to problem: https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
#Time complexity: O(n)
#Space complexity: O(n)
                        
from typing import Optional
from help.treeNodeDefinition import TreeNode
from help.seed_binary_tree import seed_binary_tree, print_binary_tree
                       
class Solution:
    def minimum_absolute_difference_in_bst(self,root:Optional[TreeNode]) -> int:
        prev = [None]
        min_value = [float("inf")]
        def inOrder(node):
           if node is None:
               return

           inOrder(node.left)
           if prev[0] is None:
                prev[0] = node.val
           else:
                min_value[0] = min(min_value[0],abs(node.val - prev[0]))
                prev[0] = node.val

           inOrder(node.right)
        
        inOrder(root)
        return min_value[0]
            
solution = Solution()
head = seed_binary_tree()
head_after = solution.minimum_absolute_difference_in_bst(head)
print_binary_tree(head_after)
    
head = seed_binary_tree()
head_after = solution.minimum_absolute_difference_in_bst(head)
print_binary_tree(head_after)
