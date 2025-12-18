#Link to problem: https://leetcode.com/problems/product-of-array-except-self/description/
#Time complexity: O(n)
#Space complexity: O(n)
                       
class Solution:
    def product_of_array_except_self(self,nums:list[int]) -> list[int]:
        result = [1 for i in range(len(nums))]

        left = 1
        right = 1

        for i in range(len(nums) - 1, -1, -1):
            result[i] = right
            right *= nums[i]
        
        for i,num in enumerate(nums):
            result[i] *= left
            left *= num

        return result
                                        
solution = Solution()
print(solution.product_of_array_except_self([1,2,3,4]))
print(solution.product_of_array_except_self([-1,1,0,-3,3]))
