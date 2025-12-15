#Link to problem: https://leetcode.com/problems/is-subsequence/description/
#Time complexity: O(k) , where k is the length of t
#Space complexity: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        elif len(s) > len(t):
            return False
        
        s_pointer = 0

        for letter in t:
            if s_pointer == len(s):
                break

            if s[s_pointer] == letter:
                s_pointer += 1

        return s_pointer == len(s)

solution = Solution()
print(solution.isSubsequence("abc","ahbgdc"))
print(solution.isSubsequence("axc","ahbgdc"))
print(solution.isSubsequence("","ahbgdc"))
print(solution.isSubsequence("axc",""))