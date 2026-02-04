#Link to problem: https://leetcode.com/problems/symmetric-tree/description/
#Time complexity: O(n)
#Space complexity: O(h), where h is the height of the tree
                        
from typing import Optional
from help.treeNodeDefinition import TreeNode
from help.seed_binary_tree import seed_binary_tree, print_binary_tree
                       
class Solution:
    def symmetric_tree(self,root:Optional[TreeNode]) -> bool:
        
        def invert_tree(root):

            if root is None:
                return

            root.left,root.right = root.right,root.left

            invert_tree(root.left)
            invert_tree(root.right)
        
        def is_equal(p,q):
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
        
        invert_tree(root.right)
        return is_equal(root.left,root.right)
                                        
solution = Solution()
head = seed_binary_tree()
head_after = solution.symmetric_tree(head)
print_binary_tree(head_after)
    
head = seed_binary_tree()
head_after = solution.symmetric_tree(head)
print_binary_tree(head_after)
