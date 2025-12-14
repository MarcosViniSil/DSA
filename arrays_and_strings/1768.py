#Link problem: https://leetcode.com/problems/merge-strings-alternately/
#Time complexity: O(N), WHERE N = len(word1) + len(word2)
#Space complexity: O(N), WHERE N = len(word1) + len(word2)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_length = min(len(word1),len(word2))

        result = []

        for i in range(min_length):
            result.append(word1[i])
            result.append(word2[i])

        if len(word1) > min_length:
            result.append(word1[min_length:])
        elif len(word2) > min_length:
            result.append(word2[min_length:])

        return ''.join(result)


solution = Solution()
print(solution.mergeAlternately("abc","pqr"))
print(solution.mergeAlternately("ab","pqrs"))