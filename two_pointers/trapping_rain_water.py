#Link to problem: https://leetcode.com/problems/trapping-rain-water/description/
#Time complexity:
#Space complexity: 
                       
class Solution:

    def trapping_rain_water(self,height:list[int]) -> int:
        if len(height) == 1:
            return 0
        result = 0
        left,right = 0, 1 
        blocks_sum = 0
        is_to_compute = -1
        has_larger = False
        while left < right and right < len(height):
            if left == 0 and height[left] == 0:
                left += 1
                right += 1

            if is_to_compute != left:
                has_larger = max(height[left+1:]) >= height[left]
                is_to_compute = left

            if height[right] >= height[left]:
                width = abs(right - left) - 1
                print("width ",width)
                min_height = min(height[left],height[right])
                print("width ",width)
                area = (min_height * width) - blocks_sum
                print(area)
                result += area
                blocks_sum = 0
                left = right
                right += 1
            elif has_larger:
                right += 1
            elif not has_larger:
                left = right
                right += 1
        
        return result

                                        
solution = Solution()
print(solution.trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]))
#print(solution.trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]))
#print(solution.trapping_rain_water([4,2,0,3,2,5]))
#print(solution.trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1,0,2,0,3]))
#print(solution.trapping_rain_water([4,2,3]))
