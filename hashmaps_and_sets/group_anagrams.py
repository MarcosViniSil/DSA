#Link to problem: https://leetcode.com/problems/group-anagrams/description/
#Time complexity:O(n * m), where n = length of strs and m = length of strs[i]
#Space complexity: O(n * m), where n = length of strs and m = length of strs[i]
                       
class Solution:
    def group_anagrams(self,strs:list[str]) -> list[list[str]]:
        if len(strs) == 1:
            return [[strs[0]]]
        
        map = {}
            
        for word in strs:
            counter = [0 for _ in range(26)]

            for letter in word:
                counter[ord(letter) - ord('a')] += 2
            
            value = '-'.join(str(v) for v in counter)
            if map.get(value) is None:
                map[value] = [word]
            else:
                 map[value].append(word)
    

        return list(map.values())

                                        
solution = Solution()
print(solution.group_anagrams(["eat","tea","tan","ate","nat","bat"]))
print(solution.group_anagrams([""]))
print(solution.group_anagrams(["a"]))
print(solution.group_anagrams(["bdddddddddd","bbbbbbbbbbc"]))