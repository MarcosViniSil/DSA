#Link to problem: https://leetcode.com/problems/rotate-image/
#Time complexity:
#Space complexity: 
                       
class Solution:
    def rotate_image(self,matrix:list[list[int]]) -> None:
        
        #Transpose matrix
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        #Swap elements from left to right
        for element in matrix:
            left = 0
            right = len(element) - 1
        
            while left < right:
                element[left],element[right] = element[right],element[left]
                left += 1
                right -= 1

        print(matrix)

solution = Solution()
print(solution.rotate_image([[1,2,3],[4,5,6],[7,8,9]]))
print(solution.rotate_image([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
