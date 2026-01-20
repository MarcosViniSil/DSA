#Link to problem: https://leetcode.com/problems/max-consecutive-ones-iii/
#Time complexity: O(n)
#Space complexity: O(1)
                       
class Solution:
    def max_consecutive_ones_iii(self,nums:list[int],k:int) -> int:
        l =0 
        zeros_count = 0
        max_ones = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros_count += 1
            
            while zeros_count > k:
                if nums[l] == 0:
                    zeros_count -= 1
                
                l += 1
            
            window_size = r - l + 1
            max_ones = max(max_ones,window_size)

        return max_ones
                                        
solution = Solution()
print(solution.max_consecutive_ones_iii([1,1,1,0,0,0,1,1,1,1,0],2))
print(solution.max_consecutive_ones_iii([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))
print(solution.max_consecutive_ones_iii([1,1,1,1,1],3))
