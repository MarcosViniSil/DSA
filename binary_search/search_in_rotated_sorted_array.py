#Link to problem: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#Time complexity: O(log(n))
#Space complexity: O(1)
                       
class Solution:
    def search_in_rotated_sorted_array(self,nums:list[int],target:int) -> int:
        left, right = 0, len(nums) - 1
        n = len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid
        
        index_min_value = left
        if index_min_value == 0:
            left,right = 0,n
        elif target >= nums[0] and target <= nums[index_min_value - 1]:
            left, right = 0, index_min_value - 1
        else:
            left, right = index_min_value, n
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
                                        
solution = Solution()
print(solution.search_in_rotated_sorted_array([4,5,6,7,0,1,2],0))
print(solution.search_in_rotated_sorted_array([4,5,6,7,0,1,2],3))
print(solution.search_in_rotated_sorted_array([4,5,6,7,0,1,2],5))
print(solution.search_in_rotated_sorted_array([4,5,6,7,0,1],7))
print(solution.search_in_rotated_sorted_array([1],0))
print(solution.search_in_rotated_sorted_array([1,3],3))
print(solution.search_in_rotated_sorted_array([1,3],1))
print(solution.search_in_rotated_sorted_array([3,1],0))
print(solution.search_in_rotated_sorted_array([3,1],4))