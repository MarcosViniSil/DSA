#Link to problem: https://leetcode.com/problems/trapping-rain-water/description/
#Time complexity: O(n)
#Space complexity: O(n)
                       
class Solution:

    def trapping_rain_water(self,height:list[int]) -> int:
        l_wall,r_wall = 0,0
        max_left =  [0] * len(height)
        max_right = [0] * len(height)
        j = len(height) - 1
        
        for i in range(len(height)):
            max_left[i] = l_wall
            max_right[j] = r_wall

            l_wall = max(l_wall,height[i])
            r_wall = max(r_wall,height[j])
            j -= 1

        result = 0
        for i in range(len(height)):
            potential = min(max_left[i],max_right[i])
            result += max(0,potential - height[i])

        return result
                                        
solution = Solution()
print(solution.trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]))
print(solution.trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]))
print(solution.trapping_rain_water([4,2,0,3,2,5]))
print(solution.trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1,0,2,0,3]))
print(solution.trapping_rain_water([4,2,3]))
