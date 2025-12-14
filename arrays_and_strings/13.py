#Link to problem: https://leetcode.com/problems/roman-to-integer/description/
#Time complexity: O(n)
#Space complexity: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        romanToInteger = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}

        actual = ""
        sum = 0
        i = 0
        while i < len(s) - 1:
            actual = s[i]+s[i+1]
            combination = romanToInteger.get(actual)
            if combination is not None:
                sum += combination
                i += 2
            else:
                sum += romanToInteger.get(s[i])
                i += 1
        
        lastPair = romanToInteger.get(s[len(s) - 2] + s[len(s) - 1])
        if lastPair is None:
            sum += romanToInteger.get(s[len(s) - 1])

        return sum



solution = Solution()
print(solution.romanToInt("III"))
print(solution.romanToInt("LVIII"))
print(solution.romanToInt("MCMXCIV"))