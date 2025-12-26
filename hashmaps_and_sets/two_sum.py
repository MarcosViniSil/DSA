#Link to problem: https://leetcode.com/problems/two-sum/description/
#Time complexity: O(n)
#Space complexity: O(n)
                       
class Solution:
    def two_sum(self,nums:list[int],target:int) -> list[int]:
        number_index = {}

        for i,number in enumerate(nums):
            number_index[number] = i
        
        for i,number in enumerate(nums):
            necessary = target - number
            
            index = number_index.get(necessary)    
            if index is not None and i != index:
                return [i,index]
        
        return []

                                        
solution = Solution()
print(solution.two_sum([2,7,11,15],9))
print(solution.two_sum([3,2,4],6))
print(solution.two_sum([3,3],6))
