#Link to problem: https://leetcode.com/problems/maximum-average-subarray-i/
#Time complexity: O(n)
#Space complexity: O(1)
                       
class Solution:
    def maximum_average_subarray_i(self,nums:list[int],k:int) -> float:
        window_sum = 0
        n = len(nums)
        
        for i in range(k):
            window_sum += nums[i]
        
        maximum_average = window_sum / k

        for i in range(n - k):
            window_sum = window_sum - nums[i] + nums[i + k]
            maximum_average = max(maximum_average, window_sum / k)
        

        return maximum_average


                                        
solution = Solution()
print(solution.maximum_average_subarray_i([1,12,-5,-6,50,3],4))
print(solution.maximum_average_subarray_i([5],1))
