#Link to problem: https://leetcode.com/problems/daily-temperatures/description/
#Time complexity: O(n)
#Space complexity: O(n)
                       
class Solution:
    def daily_temperatures(self,temperatures:list[int]) -> list[int]:
        stack = []
        res = [0] * len(temperatures)
        n = len(temperatures) - 1
        for i,temperature in enumerate(reversed(temperatures)):
            index = n - i
            
            while stack and temperatures[stack[-1]] <= temperature:
                stack.pop()
            
            if not stack:
                stack.append(index)
                continue
                
            res[index] = stack[-1] - index
            stack.append(index)
        
        return res
                              
solution = Solution()
print(solution.daily_temperatures([73,74,75,71,69,72,76,73]))
print(solution.daily_temperatures([30,40,50,60]))
print(solution.daily_temperatures([30,60,90]))
print(solution.daily_temperatures([73,73,74,75,71,69,72,76,73]))
