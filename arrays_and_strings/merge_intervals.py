#Link to problem: https://leetcode.com/problems/merge-intervals/
#Time complexity:O(n x log(n))
#Space complexity: O(n)
                       
class Solution:
    def merge_intervals(self,intervals:list[list[int]]) -> list[list[int]]:
        if len(intervals) == 1:
           return intervals
       
        intervals.sort()
        
        result = [[intervals[0][0],intervals[0][1]]]
        interval_index = 0

        for interval in intervals:
            right_elements = interval
            left_elements = result[interval_index]
            if  left_elements[1] >= right_elements[0]:
                result[interval_index][1] = max(right_elements[1],left_elements[1])
            else:
                result.append([right_elements[0],right_elements[1]])
                interval_index += 1

        return result

solution = Solution()
print(solution.merge_intervals([[1, 3], [2, 5], [6, 9]]))
print(solution.merge_intervals([[1,4],[4,5]]))
print(solution.merge_intervals([[4,7],[1,4]]))
print(solution.merge_intervals([[1,4],[2,3]]))
print(solution.merge_intervals([[4,7]]))
print(solution.merge_intervals([[1,4],[2,3]]))
