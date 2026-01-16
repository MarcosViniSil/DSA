#Link to problem: https://leetcode.com/problems/koko-eating-bananas/description/
#Time complexity: O(n.log(m)), where n is the length of piles, and m is the max value from piles
#Space complexity: O(1)

import math

class Solution:
    def koko_eating_bananas(self,piles:list[int],h:int) -> int:
        left = 1
        right = max(piles)
        min_k = float("inf")
        
        while left <= right:
            new_k = (left + right) // 2

            hours_sum = 0

            for pile in piles:
                hours_sum += math.ceil(pile / new_k)

            if hours_sum <= h:
                min_k = min(min_k,new_k)
                right = new_k - 1
            else:
                left = new_k + 1

        return min_k 

                                        
solution = Solution()
print(solution.koko_eating_bananas([3,6,7,11],8))
print(solution.koko_eating_bananas([30,11,23,4,20],5))
print(solution.koko_eating_bananas([30,11,23,4,20],6))
print(solution.koko_eating_bananas([7],6))
print(solution.koko_eating_bananas([7],6))
