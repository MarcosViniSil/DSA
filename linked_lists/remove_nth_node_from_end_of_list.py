#Link to problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#Time complexity: O(m)
#Space complexity: O(1)
                        
from typing import Optional
from help.linked_list_definition import ListNode
from help.seed_linked_list import seed, print_linked_list
                       
class Solution:
    def remove_nth_node_from_end_of_list(self,head:Optional[ListNode],n:int) -> Optional[ListNode]:
        nodes_count = 0

        aux = head

        while aux:
            nodes_count += 1
            aux = aux.next
        
        node_position = (nodes_count - n) - 1
        if node_position < 0:
            head = head.next
            return head
        
        left = head

        for _ in range(node_position):
            left = left.next

        
        left.next = left.next.next


        return head 


solution = Solution()
head = seed([1,2,3,4,5])
head_after = solution.remove_nth_node_from_end_of_list(head,1)
print_linked_list(head_after)

solution = Solution()
head = seed([1,2,3,4,5])
head_after = solution.remove_nth_node_from_end_of_list(head,2)
print_linked_list(head_after)

solution = Solution()
head = seed([1,2,3,4,5])
head_after = solution.remove_nth_node_from_end_of_list(head,3)
print_linked_list(head_after)

solution = Solution()
head = seed([1,2,3,4,5])
head_after = solution.remove_nth_node_from_end_of_list(head,4)
print_linked_list(head_after)

solution = Solution()
head = seed([1,2,3,4,5])
head_after = solution.remove_nth_node_from_end_of_list(head,5)
print_linked_list(head_after)

# ------------------ // -----------------------
solution = Solution()
head = seed([1,2,3,4])
head_after = solution.remove_nth_node_from_end_of_list(head,1)
print_linked_list(head_after)

solution = Solution()
head = seed([1,2,3,4])
head_after = solution.remove_nth_node_from_end_of_list(head,2)
print_linked_list(head_after)

solution = Solution()
head = seed([1,2,3,4])
head_after = solution.remove_nth_node_from_end_of_list(head,3)
print_linked_list(head_after)

solution = Solution()
head = seed([1,2,3,4])
head_after = solution.remove_nth_node_from_end_of_list(head,4)
print_linked_list(head_after)

    
head = seed([1])
head_after = solution.remove_nth_node_from_end_of_list(head,1)
print_linked_list(head_after)

head = seed([1,2])
head_after = solution.remove_nth_node_from_end_of_list(head,1)
print_linked_list(head_after)
