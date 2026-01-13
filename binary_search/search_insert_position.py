#Link to problem: https://leetcode.com/problems/search-insert-position/
#Time complexity:O(log(n))
#Space complexity:O(1) 
                       
class Solution:
    def search_insert_position(self,nums:list[int],target:int) -> int:
       left, right = 0, len(nums) - 1

       while left <= right:
           mid = (left + right) // 2

           if nums[mid] == target:
               return mid
           elif nums[mid] > target:
               right = mid - 1
           else:
              left = mid + 1

       return right + 1
               

                                        
solution = Solution()
print(solution.search_insert_position([1,3,5,6],7))
print(solution.search_insert_position([1,3,5,6],2))
print(solution.search_insert_position([1,3,5,6],5))
