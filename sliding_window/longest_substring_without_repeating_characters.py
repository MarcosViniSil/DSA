#Link to problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#Time complexity: O(n)
#Space complexity: O(n)

from collections import defaultdict                       
class Solution:
    def longest_substring_without_repeating_characters(self,s:str) -> int:
        frequencies = {}
        l = 0
        longest_substring = 0
        for r in range(len(s)):
            if s[r] in frequencies and frequencies[s[r]] >= l:
                l = frequencies[s[r]] + 1
            
            frequencies[s[r]] = r
            longest_substring = max(longest_substring,r - l + 1)

        return longest_substring
                                        
solution = Solution()
print(solution.longest_substring_without_repeating_characters("abcabcbb"))
print(solution.longest_substring_without_repeating_characters("bbbbb"))
print(solution.longest_substring_without_repeating_characters("pwwkew"))
print(solution.longest_substring_without_repeating_characters("p"))
print(solution.longest_substring_without_repeating_characters("dvdf"))
print(solution.longest_substring_without_repeating_characters("tmmzuxt"))
