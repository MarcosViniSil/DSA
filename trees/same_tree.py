#Link to problem: https://leetcode.com/problems/same-tree/description/
#Time complexity: O (k), where k is the min nodes between p and q
#Space complexity: O(n + m), where n is p and m is q
                        
from typing import Optional
from help.treeNodeDefinition import TreeNode
from help.seed_binary_tree import seed_binary_tree, print_binary_tree
                       
class Solution:
    def same_tree(self,p:Optional[TreeNode],q:Optional[TreeNode]) -> bool:        
        queue1 = []
        queue2 = []
        
        queue1.append(p)
        queue2.append(q)
        
        while len(queue1) > 0 and len(queue2) > 0:
            level_size = len(queue1)
            for _ in range(level_size):
                node1 = queue1.pop(0)
                node2 = queue2.pop(0)
                if node1 is None and node2 is not None:
                    return False
                if node2 is None and node1 is not None:
                    return False
                
                if node1 is None and node2 is None:
                    continue
                if node1.val != node2.val:
                    return False
                
                queue1.append(node1.left)
                queue1.append(node1.right)
                
                queue2.append(node2.left)
                queue2.append(node2.right)
        
        return len(queue1) == len(queue2)
            
                             
solution = Solution()
head = seed_binary_tree()
head_after = solution.same_tree(head)
print_binary_tree(head_after)
    
head = seed_binary_tree()
head_after = solution.same_tree(head)
print_binary_tree(head_after)
