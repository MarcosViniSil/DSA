#Link to problem: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#Time complexity: O(n)
#Space complexity: O(n)
                       
class Solution:
    def evaluate_reverse_polish_notation(self,tokens:list[int]) -> int:
        is_operator = ["+","-","*","/"]

        stack = []
        operation_result = 0
        
        for token in tokens:
            if not token in is_operator:
                stack.append(token)
            else:
                second_operating = int(stack.pop())
                first_operating = int(stack.pop())

                if token == "+":
                    operation_result = first_operating + second_operating
                elif token == "-":
                    operation_result = first_operating - second_operating
                elif token == "*":
                    operation_result = first_operating * second_operating
                else:
                    operation_result = int(first_operating / second_operating)

                stack.append(operation_result)

        return int(stack.pop())
                                        
solution = Solution()
print(solution.evaluate_reverse_polish_notation(["2","1","+","3","*"]))
print(solution.evaluate_reverse_polish_notation(["4","13","5","/","+"]))
print(solution.evaluate_reverse_polish_notation(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
