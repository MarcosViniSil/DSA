#Link to problem: https://leetcode.com/problems/squares-of-a-sorted-array/
#Time complexity: O(n)
#Space complexity: O(n)
                       
class Solution:
    def squares_of_a_sorted_array(self,nums:list[int]) -> list[int]:
        left, right = 0,len(nums) - 1
        pos = len(nums) - 1
        res = [0 for _ in range(len(nums))]

        while left <= right:
            if nums[right] ** 2 >= nums[left] ** 2:
                res[pos] = nums[right] ** 2
                pos -= 1
                right -= 1
            elif nums[left] ** 2 > nums[right] ** 2:
                res[pos] = nums[left] ** 2
                pos -= 1
                left += 1
        return res   
               
solution = Solution()
print(solution.squares_of_a_sorted_array([-4,-1,0,3,10]))
print(solution.squares_of_a_sorted_array([-7,-3,2,3,11]))
