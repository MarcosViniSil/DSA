#Link to problem: https://leetcode.com/problems/next-greater-element-i/description/
#Time complexity: O(N), where N = len(nums1) + len(nums2)
#Space complexity: O(M), where M = len(nums1)
                       
class Solution:
    def next_greater_element_i(self,nums1:list[int],nums2:list[int]) -> list[int]:
        my_map = {v:i for i,v in enumerate(nums1)}
        stack = []
        res = [-1] * len(nums1)
        
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
               val = stack.pop()
               idx = my_map[val]
               res[idx] = cur
            
            if cur in my_map:
               stack.append(cur)


        return res
                                        
solution = Solution()
print(solution.next_greater_element_i([4,1,2],[4,2,1,5,4,2]))
print(solution.next_greater_element_i([2,4],[1,2,3,4]))
