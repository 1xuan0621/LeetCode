class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        ans = 0
        i = 0
        while i < len(s) - 1:
            if s[i] == 'I' and s[i + 1] == 'V':
                ans += 4
                i += 1
            elif s[i] == 'I' and s[i + 1] == 'X':
                ans += 9
                i += 1
            elif s[i] == 'X' and s[i + 1] == 'L':
                ans += 40
                i += 1
            elif s[i] == 'X' and s[i + 1] == 'C':
                ans += 90
                i += 1
            elif s[i] == 'C' and s[i + 1] == 'D':
                ans += 400
                i += 1
            elif s[i] == 'C' and s[i + 1] == 'M':
                ans += 900
                i += 1
            else:
                ans += symbols[s[i]]
            i += 1
        if s[-2:] not in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
            ans += symbols[s[-1]]
        return ans


s = "MMCDXXV"

print(Solution().romanToInt(s))