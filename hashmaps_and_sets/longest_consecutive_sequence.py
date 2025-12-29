#Link to problem: https://leetcode.com/problems/longest-consecutive-sequence/description/
#Time complexity: O(n)
#Space complexity: O(n)
                       
from collections import defaultdict


class Solution:
    def longest_consecutive_sequence(self,nums:list[int]) -> int:
        my_map = defaultdict(bool)
        for num in nums:
            my_map[num]  = True 

        result = 0
        for num in nums:
            if not my_map[num]:
                 continue
            
            begin_sequence = num - 1

            while my_map[begin_sequence]:
                begin_sequence -= 1
            
            longest_sequence = 0
            current_number = begin_sequence + 1
            while my_map[current_number]:
                my_map[current_number] = False
                current_number += 1
                longest_sequence += 1

            result = max(result,longest_sequence)
        
        return result

                                        
solution = Solution()
print(solution.longest_consecutive_sequence([100,4,200,1,3,2]))
print(solution.longest_consecutive_sequence([0,3,7,2,5,8,4,6,0,1]))
print(solution.longest_consecutive_sequence([1,0,1,2]))
print(solution.longest_consecutive_sequence([0]))
