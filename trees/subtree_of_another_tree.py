#Link to problem: https://leetcode.com/problems/subtree-of-another-tree/description/
#Time complexity:O(n * m), where n is the root and m is the subtree nodes
#Space complexity: O(n)
                        
from typing import Optional
from help.treeNodeDefinition import TreeNode
from help.seed_binary_tree import seed_binary_tree, print_binary_tree
                       
class Solution:
    def subtree_of_another_tree(self,root:Optional[TreeNode],subRoot:Optional[TreeNode]) -> bool:
        
        def head_sub_tree(root,val):

            if not root:
                return

            if root.val == val:
                if is_sub_tree(root,subRoot):
                    return True
            
            return head_sub_tree(root.left, val) or head_sub_tree(root.right, val)

        def is_sub_tree(root,subRoot):

            if not root and not subRoot:
                return True

            if not root and subRoot:
                return False
            
            if not subRoot and root:
                return False
            
            if root.val != subRoot.val:
                return False
            
            return is_sub_tree(root.left,subRoot.left) and is_sub_tree(root.right,subRoot.right)

        if head_sub_tree(root,subRoot.val) is not None:
            return True
        
        return False
                                        
solution = Solution()
head = seed_binary_tree()
head_after = solution.subtree_of_another_tree(head)
print_binary_tree(head_after)
    
head = seed_binary_tree()
head_after = solution.subtree_of_another_tree(head)
print_binary_tree(head_after)
