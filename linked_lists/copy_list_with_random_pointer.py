#Link to problem: https://leetcode.com/problems/copy-list-with-random-pointer/
#Time complexity:
#Space complexity: 
                        
from typing import Optional
from help.linked_list_definition import Node
from help.seed_linked_list import seed, print_linked_list
                       
class Solution:
    def copy_list_with_random_pointer(self,head:Optional[Node]) -> Optional[Node]:
        pass

                                        
solution = Solution()
head = seed()
head_after = solution.copy_list_with_random_pointer(head)
print_linked_list(head_after)
    
head = seed()
head_after = solution.copy_list_with_random_pointer(head)
print_linked_list(head_after)
