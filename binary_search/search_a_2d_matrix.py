#Link to problem: https://leetcode.com/problems/search-a-2d-matrix/description/
#Time complexity: O(log(m) + log(n)) = O(log(m.n)), where m = rows, n = columns
#Space complexity: O(1)
                       
class Solution:
    def search_a_2d_matrix(self,matrix:list[list[int]],target:int) -> bool:
        left = 0
        right = len(matrix) - 1
        row = 0     
        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] == target or matrix[mid][len(matrix[0]) - 1] == target:
                return True
            elif matrix[mid][0] < target and matrix[mid][len(matrix[0]) - 1] > target:
                row = mid
                break
            elif matrix[mid][len(matrix[0]) - 1] < target:
                left = mid + 1
            else:
                right = mid - 1

        left = 0
        right = len(matrix[0]) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False

        

                                        
solution = Solution()
#print(solution.search_a_2d_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
#print(solution.search_a_2d_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))
#print(solution.search_a_2d_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],1))
#print(solution.search_a_2d_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],11))
#print(solution.search_a_2d_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],60))
#print(solution.search_a_2d_matrix([[1,3,5]],3))
#print(solution.search_a_2d_matrix([[3]],3))
print(solution.search_a_2d_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],5))
