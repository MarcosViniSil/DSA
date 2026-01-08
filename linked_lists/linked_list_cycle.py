#Link to problem: https://leetcode.com/problems/linked-list-cycle/description/
#Time complexity: O(n)
#Space complexity:O(1) 
                        
from typing import Optional
from help.linked_list_definition import ListNode
from help.seed_linked_list import seed_index
                       
class Solution:
    def linked_list_cycle(self,head:Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow = head
        fast = head.next

        while fast and fast.next:

            if slow == fast:
                return True
            
            fast = fast.next.next
            slow = slow.next

        return False

                      
solution = Solution()
head = seed_index([3,2,0,-4],1)
print(solution.linked_list_cycle(head))
    
head = seed_index([1,2],0)
print(solution.linked_list_cycle(head))

head = seed_index([1],-1)
print(solution.linked_list_cycle(head))
