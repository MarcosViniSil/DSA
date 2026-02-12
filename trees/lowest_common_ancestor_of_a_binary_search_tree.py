#Link to problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
#Time complexity:
#Space complexity: 
                        
from typing import Optional
from help.treeNodeDefinition import TreeNode
from help.seed_binary_tree import seed_binary_tree, print_binary_tree
                       
class Solution:
    def lowest_common_ancestor_of_a_binary_search_tree(self,root:Optional[TreeNode],p:Optional[TreeNode],q:Optional[TreeNode]) -> Optional[TreeNode]:
        
        lca = [-1]
        
        def call(root):
            
            if root is None:
                return
            
            lca[0] = root.val

            if root is p or root is q:
                return
            elif root.val > p.val and root.val > q.val:
                call(root.left)
            elif root.val < p.val and root.val < q.val:
                call(root.right)
            else:
                return
    
        call(root)
        return lca[0]
                                        
solution = Solution()
head = seed_binary_tree()
head_after = solution.lowest_common_ancestor_of_a_binary_search_tree(head)
print_binary_tree(head_after)
    
head = seed_binary_tree()
head_after = solution.lowest_common_ancestor_of_a_binary_search_tree(head)
print_binary_tree(head_after)
