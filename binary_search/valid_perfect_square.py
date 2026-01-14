#Link to problem: https://leetcode.com/problems/valid-perfect-square/description/
#Time complexity:  O(log(n))
#Space complexity: O(1)
                       
class Solution:
    def valid_perfect_square(self,num:int) -> bool:
        left, right = 1,num

        while left <= right:

            mid = (left + right) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1

        return False

                                        
solution = Solution()
print(solution.valid_perfect_square(16))
print(solution.valid_perfect_square(14))
print(solution.valid_perfect_square(1))
print(solution.valid_perfect_square(2))
print(solution.valid_perfect_square(4))
