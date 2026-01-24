#Link to problem: https://leetcode.com/problems/longest-repeating-character-replacement/description/
#Time complexity: O(n)
#Space complexity: O(1)
                       
class Solution:
    def longest_repeating_character_replacement(self,s:str,k:int) -> int:
        left = 0
        frequency = [0 for _ in range(26)]
        max_frequency = 0
        longest_repeating = 0
        
        for right in range(len(s)):
            frequency[ord(s[right]) - ord('A')] += 1

            max_frequency = max(max_frequency,frequency[ord(s[right])- ord('A')])

            while (right - left + 1) - max_frequency > k:
                frequency[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            longest_repeating = max(longest_repeating,right - left + 1)

        return longest_repeating

                            
solution = Solution()
print(solution.longest_repeating_character_replacement("ABAB",2))
print(solution.longest_repeating_character_replacement("AABABBA",1))
print(solution.longest_repeating_character_replacement("AABABBA",2))
print(solution.longest_repeating_character_replacement("ABCCCCA",2))
print(solution.longest_repeating_character_replacement("AAAAAAA",2))
print(solution.longest_repeating_character_replacement("ABBB",3))
print(solution.longest_repeating_character_replacement("A",3))