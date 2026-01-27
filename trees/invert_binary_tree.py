#Link to problem: https://leetcode.com/problems/invert-binary-tree/
#Time complexity:
#Space complexity: 
                        
from typing import Optional
from help.treeNodeDefinition import TreeNode
from help.seed_binary_tree import seed_binary_tree, print_binary_tree
                       
class Solution:
    def invert_binary_tree(self,root:Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left,root.right = root.right,root.left

        self.invert_binary_tree(root.left)
        self.invert_binary_tree(root.right)

        return root

                                        
solution = Solution()
head = seed_binary_tree([4,2,7,1,3,6,9])
head_after = solution.invert_binary_tree(head)
print_binary_tree(head_after)
    
head = seed_binary_tree([2,1,3])
head_after = solution.invert_binary_tree(head)
print_binary_tree(head_after)

head = seed_binary_tree([])
head_after = solution.invert_binary_tree(head)
print_binary_tree(head_after)
