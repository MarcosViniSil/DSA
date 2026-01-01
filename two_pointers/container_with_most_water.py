#Link to problem: https://leetcode.com/problems/container-with-most-water/description/
#Time complexity:
#Space complexity: 
                       
class Solution:
    def container_with_most_water(self,height:list[int]) -> int:
        max_area = 0

        left, right = 0, len(height) - 1

        while left < right:

            area = min(height[left],height[right]) * (right - left)
            max_area = max(max_area,area)

            if height[left] == height[right]:
                left += 1
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


                                        
solution = Solution()
print(solution.container_with_most_water([1,8,6,2,5,4,8,3,7]))
print(solution.container_with_most_water([1,1]))
print(solution.container_with_most_water([3,8,6,2,5,4,8,7,3]))
