#Link to problem: https://leetcode.com/problems/validate-binary-search-tree/
#Time complexity: O(n)
#Space complexity: O(n)
                        
from typing import Optional
from help.treeNodeDefinition import TreeNode
from help.seed_binary_tree import seed_binary_tree, print_binary_tree
                       
class Solution:
    def validate_binary_search_tree(self,root:Optional[TreeNode]) -> bool:
        
        prev = [None] 
        res = [True]       
        def valid_bst(root:Optional[TreeNode]):

            if root is None:
                return
            
            valid_bst(root.left)
            
            if prev[0] is None:
                prev[0] = root.val
            else:
                if root.val <= prev[0]:
                    res[0] = False
                    return False
                prev[0] = root.val    
            
            valid_bst(root.right)
        
        valid_bst(root) 
        return res[0]    
                                        
solution = Solution()
head = seed_binary_tree()
head_after = solution.validate_binary_search_tree(head)
print_binary_tree(head_after)
    
head = seed_binary_tree()
head_after = solution.validate_binary_search_tree(head)
print_binary_tree(head_after)
