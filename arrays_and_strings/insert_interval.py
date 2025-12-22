#Link to problem: https://leetcode.com/problems/insert-interval/description/
#Time complexity:
#Space complexity: 
                       
class Solution:

    def binary_search(intervals:list[list[int]],newInterval:list[int]) -> int:
        
        low  = 0
        high = len(intervals) - 1

        while low < high:
            middle = (low + high) // 2

            

    def insert_interval(self,intervals:list[list[int]],newInterval:list[int]) -> list[list[int]]:
        pass

                                        
solution = Solution()
print(solution.insert_interval([[1,3],[6,9]],[2,5]))
print(solution.insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
