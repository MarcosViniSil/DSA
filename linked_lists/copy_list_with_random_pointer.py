#Link to problem: https://leetcode.com/problems/copy-list-with-random-pointer/
#Time complexity: O(n)
#Space complexity: O(n)
                        
from typing import Optional
from help.linked_list_definition import Node
from help.seed_linked_list import seed, print_linked_list
                       
class Solution:
    def copy_list_with_random_pointer(self,head:Optional[Node]) -> Optional[Node]:
        if head is None:
            return head
    
        head_aux = head
        nodes_stored = {}
        
        while head_aux:
            node = Node(head_aux.val)
            nodes_stored[head_aux] = node
            head_aux = head_aux.next

        head_aux = head
        while head_aux:
            new_node = nodes_stored[head_aux]
            new_node.next = nodes_stored[head_aux.next] if head_aux.next else None
            new_node.random = nodes_stored[head_aux.random] if head_aux.random else None
            head_aux = head_aux.next
        
        return nodes_stored[head]
                                        
solution = Solution()
head = seed()
head_after = solution.copy_list_with_random_pointer(head)
print_linked_list(head_after)
    
head = seed()
head_after = solution.copy_list_with_random_pointer(head)
print_linked_list(head_after)
