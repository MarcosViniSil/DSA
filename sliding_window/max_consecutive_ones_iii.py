#Link to problem: https://leetcode.com/problems/max-consecutive-ones-iii/
#Time complexity:
#Space complexity: 
                       
class Solution:
    def max_consecutive_ones_iii(self,nums:list[int],k:int) -> int:
        start,end = 0, 0

        zeros_flipped = 0
        max_sum = 0
        window_size = 0
        index_earliest_zero = 0
        for i in range(len(nums)):

            if end >= len(nums):
                break

            while start <= end and end < len(nums):
                if zeros_flipped ==k:
                    break
                if nums[end] == 1:
                    window_size += 1
                elif nums[end] == 0 and zeros_flipped < k:
                    window_size += 1
                    zeros_flipped += 1
                    
                    index_earliest_zero = start
                end += 1
            
            print("index_earliest_zero ",index_earliest_zero)
            max_sum = max(max_sum,window_size)
            start = index_earliest_zero + 1
            end = start    

            window_size = 0
            zeros_flipped = 0
            index_earliest_zero = 0

        max_sum = max(max_sum,window_size)

        return max_sum

                                        
solution = Solution()
#print(solution.max_consecutive_ones_iii([1,1,1,0,0,0,1,1,1,1,0],2))
print(solution.max_consecutive_ones_iii([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))
#print(solution.max_consecutive_ones_iii([1,1,1,1,1],3))
