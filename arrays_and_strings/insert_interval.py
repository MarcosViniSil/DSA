#Link to problem: https://leetcode.com/problems/insert-interval/description/
#Time complexity: O(n)
#Space complexity: O(n)
                       
class Solution:

    def binary_search(self,intervals:list[list[int]],newInterval:list[int]) -> int:
        
        low  = 0
        high = len(intervals) - 1

        while low <= high:
            middle = (low + high) // 2

            if intervals[middle][0] == newInterval[0]:
                if intervals[middle][1] >= newInterval[1]:
                    return middle
                else:
                    return middle + 1
                
            elif intervals[middle][0] < newInterval[0]:
                low = middle + 1
            else:
                high = middle - 1
            
        return low

    def insert_interval(self,intervals:list[list[int]],newInterval:list[int]) -> list[list[int]]:
        index = self.binary_search(intervals=intervals,newInterval=newInterval) # 0(log(n))

        intervals.insert(index,newInterval) # O(n)

        if len(intervals) <= 1:
            return intervals

        left_element = intervals[0][0]
        right_element = intervals[0][1]

        response = [[left_element,right_element]]
        interval_index = 0

        for interval in intervals: # O(n)
            left_elements = response[interval_index]
            right_elements = interval

            if left_elements[1] >= right_elements[0]:
                response[interval_index][1] = max(left_elements[1],right_elements[1])
            else:
                response.append(interval)
                interval_index += 1

        return response

                                        
solution = Solution()
print(solution.insert_interval([[1,3],[6,9]],[2,5]))
print(solution.insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
print(solution.insert_interval([[2,5],[6,9]],[2,4]))
print(solution.insert_interval([],[2,4]))
print(solution.insert_interval([],[]))
