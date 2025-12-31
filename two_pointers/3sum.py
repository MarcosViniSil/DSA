#Link to problem: https://leetcode.com/problems/3sum/description/
#Time complexity: O(n^2)
#Space complexity: O(n)
                       
class Solution:
    def sum3(self,nums:list[int]) -> list[list[int]]:
        nums.sort()
        i = 1
        my_map = set()

        while i < len(nums):
            
            target = nums[i - 1]
            if target > 0:
                 break          
            
            left = i 
            right = len(nums) - 1
            while left < right:
                if (nums[left],nums[right],target) in my_map:
                        left  += 1
                        right -= 1
                        continue

                if nums[left] + nums[right] + target == 0:
                    my_map.add((nums[left],nums[right],target))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] + target < 0:
                    left += 1
                else:
                    right -= 1
            i += 1
        return list(map(lambda e: list(e), my_map))

                                        
solution = Solution()
print(solution.sum3([-1,0,1,2,-1,-4]))
print(solution.sum3([-5,-5,-4,-4,9,9,10]))
print(solution.sum3([0,1,1]))
print(solution.sum3([0,0,0]))
print(solution.sum3([12,21,43,67,9]))
print(solution.sum3([1,2,-2,-1]))
print(solution.sum3([1,1,-2]))
print(solution.sum3([-100,-70,-60,110,120,130,160]))
print(solution.sum3([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))
