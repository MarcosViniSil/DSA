#Link to problem: https://leetcode.com/problems/diameter-of-binary-tree/description/
#Time complexity: O(n)
#Space complexity: O(h), where h is the height of the tree
                        
from typing import Optional
from help.treeNodeDefinition import TreeNode
from help.seed_binary_tree import seed_binary_tree, print_binary_tree
                       
class Solution:
    def diameter_of_binary_tree(self,root:Optional[TreeNode]) -> int:
        res = [0]
        def call(root):
            if root is None:
                return 0

            left = call(root.left)
            right = call(root.right)

            max_value = left + right
            res[0] = max(res[0],max_value)

            return max(left,right) + 1

        call(root)
        return res[0]
                                        
solution = Solution()
head = seed_binary_tree()
head_after = solution.diameter_of_binary_tree(head)
print_binary_tree(head_after)
    
head = seed_binary_tree()
head_after = solution.diameter_of_binary_tree(head)
print_binary_tree(head_after)
