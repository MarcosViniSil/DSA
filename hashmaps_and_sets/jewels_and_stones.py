#Link to problem: https://leetcode.com/problems/jewels-and-stones/description/
#Time complexity: O(N), where N = len(jewels) + len(stones)
#Space complexity: O(K), where k = len(stones)
                       
class Solution:
    def jewels_and_stones(self,jewels:str,stones:str) -> int:
        map = {}

        for stone in stones:
            if map.get(stone) is None:
                map[stone] = 1
            else:
                map[stone] += 1
        
        res = 0

        for jewel in jewels:
            if map.get(jewel) is not None:
                res += map.get(jewel)

        return res
                                        
solution = Solution()
print(solution.jewels_and_stones("aA","aAAbbbb"))
print(solution.jewels_and_stones("z","ZZ"))
