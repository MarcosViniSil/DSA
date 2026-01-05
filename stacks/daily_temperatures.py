#Link to problem: https://leetcode.com/problems/daily-temperatures/description/
#Time complexity:
#Space complexity: 
                       
class Solution:
    def daily_temperatures(self,temperatures:list[int]) -> list[int]:
        my_map = {v:i for i,v in enumerate(temperatures)}
        stack = []

        
                              
solution = Solution()
print(solution.daily_temperatures([73,74,75,71,69,72,76,73]))
print(solution.daily_temperatures([30,40,50,60]))
print(solution.daily_temperatures([30,60,90]))

#[1212,0,0,0,0,0,0,0]
#      ^