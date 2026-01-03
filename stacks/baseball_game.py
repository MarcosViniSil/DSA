#Link to problem: https://leetcode.com/problems/baseball-game/description/
#Time complexity: O(n)
#Space complexity: O(n)
                       
class Solution:
    def baseball_game(self,operations:list[str]) -> int:
        stack = []

        for operation in operations:
        
            if operation.lstrip("-").isdigit():
                stack.append(int(operation))
            elif operation == "+":
                sum_digits = stack[-1] + stack[-2]
                stack.append(sum_digits)
            elif operation == "D":
                double_previous = stack[-1] * 2
                stack.append(double_previous)
            elif operation == "C":
                stack.pop()
        return sum(stack)
                                        
solution = Solution()
print(solution.baseball_game(["5","2","C","D","+"]))
print(solution.baseball_game(["1","C"]))
print(solution.baseball_game(["5","-2","4","C","D","9","+","+"]))
