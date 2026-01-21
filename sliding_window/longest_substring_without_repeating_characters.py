#Link to problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#Time complexity: O(n)
#Space complexity: O(1)

from collections import defaultdict                       
class Solution:
    def longest_substring_without_repeating_characters(self,s:str) -> int:
        last_index = {}
        l = 0
        max_substring = 0

        for r in range(len(s)):
            if s[r] in last_index and last_index[s[r]] >= l:
                l = last_index[s[r]] + 1

            last_index[s[r]] = r
            max_substring = max(max_substring, r - l + 1)

        return max_substring
                                        
solution = Solution()
print(solution.longest_substring_without_repeating_characters("abcabcbb"))
print(solution.longest_substring_without_repeating_characters("bbbbb"))
print(solution.longest_substring_without_repeating_characters("pwwkew"))
print(solution.longest_substring_without_repeating_characters("p"))
print(solution.longest_substring_without_repeating_characters("dvdf"))
print(solution.longest_substring_without_repeating_characters("tmmzuxt"))
