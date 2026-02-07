#Link to problem: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
#Time complexity: O(n)
#Space complexity: O(n)
                        
from typing import Optional
from help.treeNodeDefinition import TreeNode
from help.seed_binary_tree import seed_binary_tree, print_binary_tree
                       
class Solution:
    def kth_smallest_element_in_a_bst(self,root:Optional[TreeNode],k:int) -> int:
        stack = []
        curr = root
        index = 0
        while curr or len(stack) > 0:
            
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            index = index + 1
            if index == k:
                return curr.val
            
            curr = curr.right

        return -1
                                        
solution = Solution()
head = seed_binary_tree()
head_after = solution.kth_smallest_element_in_a_bst(head)
print_binary_tree(head_after)
    
head = seed_binary_tree()
head_after = solution.kth_smallest_element_in_a_bst(head)
print_binary_tree(head_after)
