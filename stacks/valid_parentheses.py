#Link to problem: https://leetcode.com/problems/valid-parentheses/
#Time complexity: O(n)
#Space complexity: O(n)
                 
class Solution:
    def valid_parentheses(self,s:str) -> bool:
        is_open =  ["{","(","["]
        is_close = {"}":"{",")":"(","]":"["}
        
        stack = []

        for c in s:
            if c in is_open:
                stack.append(c)
            elif c in is_close:
                if len(stack) == 0 or is_close.get(c) != stack.pop():
                    return False

        return len(stack) == 0
                                        
solution = Solution()
print(solution.valid_parentheses("()"))
print(solution.valid_parentheses("()[]{}"))
print(solution.valid_parentheses("(]"))
print(solution.valid_parentheses("([])"))
print(solution.valid_parentheses("([)]"))
print(solution.valid_parentheses("(("))
