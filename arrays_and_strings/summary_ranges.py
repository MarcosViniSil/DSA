#Link to problem: https://leetcode.com/problems/summary-ranges/description/
#Time complexity: O(n)
#Space complexity: O(n)
                       
class Solution:
    def summary_ranges(self,nums:list[str]) -> list[str]:
        if len(nums) == 0:
            return []

        begin_sequence = nums[0]
        end_sequence = nums[0]
        sequence = ""
        ranges = []
        
        for num in nums:
            if num > end_sequence + 1:
                sequence = f"{begin_sequence}->{end_sequence}" if begin_sequence != end_sequence else f"{begin_sequence}"
                ranges.append(sequence)
                begin_sequence = num
            
            end_sequence = num
        
        sequence = f"{begin_sequence}->{end_sequence}" if begin_sequence != end_sequence else f"{begin_sequence}"
        ranges.append(sequence)
        
        return ranges
                                        
solution = Solution()
print(solution.summary_ranges([0,1,2,4,5,7]))
print(solution.summary_ranges([0,2,4,6,8,10,12,14]))
print(solution.summary_ranges([0]))
print(solution.summary_ranges([]))
