#Link to problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#Time complexity: O(log(n))
#Space complexity: O(1)
                       
class Solution:
    def find_minimum_in_rotated_sorted_array(self,nums:list[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[right]

                                        
solution = Solution()
print(solution.find_minimum_in_rotated_sorted_array([3,4,5,1,2]))
print(solution.find_minimum_in_rotated_sorted_array([4,5,6,7,0,1,2]))
print(solution.find_minimum_in_rotated_sorted_array([11,13,15,17]))
print(solution.find_minimum_in_rotated_sorted_array([11]))
print(solution.find_minimum_in_rotated_sorted_array([1,2,3,4,5]))
print(solution.find_minimum_in_rotated_sorted_array([2,3,4,5,1]))
print(solution.find_minimum_in_rotated_sorted_array([5,1,2,3,4]))
print(solution.find_minimum_in_rotated_sorted_array([4,5,7,9,11,2,3]))
