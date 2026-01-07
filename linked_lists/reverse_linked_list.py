#Link to problem: https://leetcode.com/problems/reverse-linked-list/description/
#Time complexity:O(n)
#Space complexity:O(1) 

from typing import Optional
from help.linked_list_definition import ListNode
from help.seed_linked_list import seed, print_linked_list

class Solution:
    def reverse_linked_list(self,head:Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        prev = None
        actual = head
        next = head.next
        
        while next:
            next = actual.next
            actual.next = prev
            prev = actual
            actual = next
            
        return prev
        
                                 
solution = Solution()

head = seed([1,2,3,4,5])
head_after = solution.reverse_linked_list(head)
print_linked_list(head_after)

head = seed([1,2])
head_after = solution.reverse_linked_list(head)
print_linked_list(head_after)

head = seed([])
head_after = solution.reverse_linked_list(head)
print_linked_list(head_after)