#Link to problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#Time complexity: O(n)
#Space complexity: O(h), where h is the height of the tree
                        
from typing import Optional
from help.treeNodeDefinition import TreeNode
from help.seed_binary_tree import seed_binary_tree, print_binary_tree
                       
class Solution:
    def maximum_depth_of_binary_tree(self,root:Optional[TreeNode]) -> int:
        
        def call(root:Optional[TreeNode],depth:int):
            if root is None:
                return depth
            
            left_max = call(root.left,depth + 1)
            right_max = call(root.right,depth + 1)
            
            max_depth = max(left_max,right_max)
            return max_depth

        return call(root,0)

solution = Solution()
head = seed_binary_tree([3,9,20,None,None,15,7])
print(solution.maximum_depth_of_binary_tree(head))

 
head = seed_binary_tree([1,None,2])
print(solution.maximum_depth_of_binary_tree(head))

