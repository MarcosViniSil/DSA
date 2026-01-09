#Link to problem: https://leetcode.com/problems/middle-of-the-linked-list/description/
#Time complexity:  O(n)
#Space complexity: O(1)
                        
from typing import Optional
from help.linked_list_definition import ListNode
from help.seed_linked_list import seed, print_linked_list
                       
class Solution:
    def middle_of_the_linked_list(self,head:Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
                                        
solution = Solution()
head = seed([1,2,3,4,5])
head_after = solution.middle_of_the_linked_list(head)
print_linked_list(head_after)
    
head = seed([1,2,3,4,5,6])
head_after = solution.middle_of_the_linked_list(head)
print_linked_list(head_after)

head = seed([1,2,3])
head_after = solution.middle_of_the_linked_list(head)
print_linked_list(head_after)

head = seed([1,2])
head_after = solution.middle_of_the_linked_list(head)
print_linked_list(head_after)

head = seed([])
head_after = solution.middle_of_the_linked_list(head)
print_linked_list(head_after)