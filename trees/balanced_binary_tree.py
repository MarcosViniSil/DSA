#Link to problem: https://leetcode.com/problems/balanced-binary-tree/description/
#Time complexity:
#Space complexity: 
                        
from typing import Optional
from help.treeNodeDefinition import TreeNode
from help.seed_binary_tree import seed_binary_tree, print_binary_tree
                       
class Solution:
    def balanced_binary_tree(self,root:Optional[TreeNode]) -> bool:
        
        def max_depth(root,depth):
            if root is None:
                return depth
            
            max_left  = max_depth(root.left,depth + 1)
            max_right = max_depth(root.right,depth + 1)
            
            return max(max_left,max_right)
            
        def call(root):

            if root is None:
                return True
            
            max_left  = max_depth(root.left,0)
            max_right = max_depth(root.right,0)
            
            if abs(max_left - max_right) > 1:
                return False

            return call(root.left) and call(root.right)
            

        res = call(root)
        if res is None:
            return True
        else:
            return False  

                                        
solution = Solution()
head = seed_binary_tree([3,9,20,None,None,15,7])
print(solution.balanced_binary_tree(head))
    
head = seed_binary_tree([1,2,2,3,3,None,None,4,4])
print(solution.balanced_binary_tree(head))

head = seed_binary_tree([])
print(solution.balanced_binary_tree(head))

