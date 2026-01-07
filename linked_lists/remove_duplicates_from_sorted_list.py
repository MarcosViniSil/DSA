#Link to problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#Time complexity: O(n)
#Space complexity: O(1)

from typing import Optional
from help.linked_list_definition import ListNode
from help.seed_linked_list import seed, print_linked_list

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
                       
class Solution:
    def remove_duplicates_from_sorted_list(self,head:Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = head
        actual = head.next
        
        while prev and actual:
            if prev.val != actual.val:
                prev.next = actual
                prev = actual
                actual = actual.next
            else:
                actual = actual.next
        
        prev.next = actual   
        
        return head

                                        
solution = Solution()
head = seed([1,1,2])
head_after = solution.remove_duplicates_from_sorted_list(head)
print_linked_list(head_after)


head = seed([1,1,2,3,3])
head_after = solution.remove_duplicates_from_sorted_list(head)
print_linked_list(head_after)
