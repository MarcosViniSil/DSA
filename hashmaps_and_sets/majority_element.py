#Link to problem: https://leetcode.com/problems/majority-element/
#Time complexity: O(n)
#Space complexity: O(1)
                       
class Solution:
    def majority_element(self,nums:list[int]) -> int:
        counter = [nums[0],0]

        for num in nums:
            if num == counter[0]:
                counter[1] += 1
            else:
                counter[1] -= 1
                if counter[1] == 0:
                    counter[0] = num
                    counter[1] += 1
        

        return counter[0]

        

                                        
solution = Solution()
print(solution.majority_element([3,2,3]))
print(solution.majority_element([2,2,1,1,1,2,2]))
print(solution.majority_element([2]))
