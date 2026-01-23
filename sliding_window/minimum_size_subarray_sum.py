#Link to problem: https://leetcode.com/problems/minimum-size-subarray-sum/description/
#Time complexity: O(n)
#Space complexity: O(1)
                       
class Solution:
    def minimum_size_subarray_sum(self,target:int,nums:list[int]) -> int:
        left = 0
        window_sum = 0
        minimum_size = float("inf")

        for right in range(len(nums)):
            
            window_sum += nums[right]

            while window_sum >= target:
                minimum_size = min(minimum_size,right - left + 1)
                window_sum -= nums[left]
                left += 1
                
        return minimum_size if minimum_size != float("inf") else 0
                                        
solution = Solution()
print(solution.minimum_size_subarray_sum(7,[2,3,1,2,4,3]))
print(solution.minimum_size_subarray_sum(4,[1,4,4]))
print(solution.minimum_size_subarray_sum(11,[1,1,1,1,1,1,1,1]))
print(solution.minimum_size_subarray_sum(11,[11]))
