# Link to problem: https://leetcode.com/problems/find-closest-number-to-zero/description/
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = float("-inf")

        for num in nums:
            if abs(num) < abs(closest):
                closest = num
        
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest
        


solution = Solution()
print(solution.findClosestNumber([2,-1,1])) # 1
print(solution.findClosestNumber([-4,-2,1,4,8]))# 1