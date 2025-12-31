#Link to problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
#Time complexity: O(n)
#Space complexity: O(1)
                       
class Solution:
    def two_sum_ii_input_array_is_sorted(self,numbers:list[int],target:int) -> list[int]:
        left,right = 0, len(numbers) - 1

        while left < right:

            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

        return []
                                        
solution = Solution()
print(solution.two_sum_ii_input_array_is_sorted([2,7,11,15],9))
print(solution.two_sum_ii_input_array_is_sorted([2,3,4],6))
print(solution.two_sum_ii_input_array_is_sorted([-1,0],-1))
