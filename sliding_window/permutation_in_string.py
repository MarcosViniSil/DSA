#Link to problem: https://leetcode.com/problems/permutation-in-string/description/
#Time complexity: O(n)
#Space complexity: O(1)

class Solution:
    def permutation_in_string(self,s1:str,s2:str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        key_s1 = [0] * 26
        key = [0] * 26

        for letter in s1:
            key_s1[ord(letter) - ord('a')] += 1
        
        right = 0
        while right < len(s1):
            key[ord(s2[right]) - ord('a')] += 1
            right += 1
        
        while right < len(s2):
            if key != key_s1:
                key[ord(s2[left]) - ord('a')] -= 1
                key[ord(s2[right]) - ord('a')] += 1
                left += 1
            
            right += 1
        
        if key == key_s1:
            return True
        else:
            return False

                                        
solution = Solution()
print(solution.permutation_in_string("ab","eidbaooo"))
print(solution.permutation_in_string("ab","eidboaoo"))
print(solution.permutation_in_string("ab","eidbaoba"))
print(solution.permutation_in_string("ab","eidbaoba"))
print(solution.permutation_in_string("eidbaoba","ab"))
print(solution.permutation_in_string("ab","abfjdhfduifys"))
print(solution.permutation_in_string("ab","fjdhfduifys"))
print(solution.permutation_in_string("adc","dcda"))
print(solution.permutation_in_string("trinitrophenylmethylnitramine","dinitrophenylhydrazinetrinitrophenylmethylnitramine"))
print(solution.permutation_in_string("ky","ainwkckifykxlribaypk"))