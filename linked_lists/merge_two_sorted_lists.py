#Link to problem: https://leetcode.com/problems/merge-two-sorted-lists/description/
#Time complexity:  O(N), where N = min(len(list1),len(list2))
#Space complexity: O(M), where M = len(list1) + len(list2)
                        
from typing import Optional
from help.linked_list_definition import ListNode
from help.seed_linked_list import seed, print_linked_list
                       
class Solution:
    def merge_two_sorted_lists(self,list1:Optional[ListNode],list2:Optional[ListNode]) -> Optional[ListNode]:
        list1_aux = list1
        list2_aux = list2

        res = ListNode()
        aux = res
        
        while list1_aux and list2_aux:
            if list1_aux.val < list2_aux.val:
                res.next = list1_aux
                list1_aux = list1_aux.next
            else:
                res.next = list2_aux
                list2_aux = list2_aux.next
            
            res = res.next

        if list1_aux:
            res.next = list1_aux
        elif list2_aux:
            res.next = list2_aux
        
        return aux.next
                                        
solution = Solution()
head1 = seed([1,2,3,4])
head2 = seed([1,2,3,4])
head_after = solution.merge_two_sorted_lists(head1,head2)
print_linked_list(head_after)

head1 = seed([])
head2 = seed([])
head_after = solution.merge_two_sorted_lists(head1,head2)
print_linked_list(head_after)

head1 = seed([])
head2 = seed([0])
head_after = solution.merge_two_sorted_lists(head1,head2)
print_linked_list(head_after)