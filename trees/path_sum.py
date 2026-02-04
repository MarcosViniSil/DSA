#Link to problem: https://leetcode.com/problems/path-sum/description/
#Time complexity: O(n)
#Space complexity: O(h) where h is the height of the tree
                        
from typing import Optional
from help.treeNodeDefinition import TreeNode
from help.seed_binary_tree import seed_binary_tree, print_binary_tree
                       
class Solution:
    def path_sum(self,root:Optional[TreeNode],targetSum:int) -> bool:
        res = [False]
        def sum_tree(root,sum_nodes):

            if not root:
                return

            if root and (root.left is None and root.right is None):

                if sum_nodes + root.val == targetSum:
                    res[0] = True

                return

            sum_nodes += root.val

            sum_tree(root.left,sum_nodes)
            sum_tree(root.right,sum_nodes)               

        sum_tree(root,0)
        return res[0]        
                                        
solution = Solution()
head = seed_binary_tree()
head_after = solution.path_sum(head)
print_binary_tree(head_after)
    
head = seed_binary_tree()
head_after = solution.path_sum(head)
print_binary_tree(head_after)
