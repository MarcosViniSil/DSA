#Link to problem: https://leetcode.com/problems/first-bad-version/description/
#Time complexity: O(log(n))
#Space complexity: O(1)

from help.isBadVersion_definition import isBadVersion

class Solution:
    def first_bad_version(self,n:int) -> int:
        left = 0
        right = n - 1

        while left <= right:

            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left + 1
                                        
solution = Solution()
print(solution.first_bad_version(5))
#print(solution.first_bad_version(1))
