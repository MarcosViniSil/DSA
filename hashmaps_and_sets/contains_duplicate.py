#Link to problem: https://leetcode.com/problems/contains-duplicate/description/
#Time complexity: O(n)
#Space complexity: O(n)
                       
class Solution:
    def contains_duplicate(self,nums:list[int]) -> bool:
        map = {}

        for num in nums:
            value = map.get(num)
            print(value)
            if value is None:
                map[num] = 1
            else:
                
                if value + 1 >= 2:
                    return True
                map[num] += 1

        return False
                                        
solution = Solution()
print(solution.contains_duplicate([1,2,3,1]))
print(solution.contains_duplicate([1,2,3,4]))
