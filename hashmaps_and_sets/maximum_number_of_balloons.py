#Link to problem: https://leetcode.com/problems/maximum-number-of-balloons/
#Time complexity:
#Space complexity: 
                       
class Solution:
    def maximum_number_of_balloons(self,text:str) -> int:
        word = "balloon"
        if len(text) < len(word):
            return 0
        
        letters_count = [0 for _ in range(27)]
        a_asc_code = ord('a')

        word_count = [0 for _ in range(27)]

        for letter in word:
            word_count[ord(letter) - a_asc_code] += 1

        word = set(word)

        for letter in text:
            letters_count[ord(letter) - a_asc_code] += 1

        res = 0
        while(True):
            for letter in word:
                idx = ord(letter) - a_asc_code
                if letters_count[idx] - word_count[idx] < 0:
                    return res
                letters_count[idx] -= word_count[idx]
            res += 1
        
                                        
solution = Solution()
print(solution.maximum_number_of_balloons("nlaebolko"))
print(solution.maximum_number_of_balloons("loonbalxballpoon"))
print(solution.maximum_number_of_balloons("leetcode"))
