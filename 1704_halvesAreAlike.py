class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count = 0
        a = s[:len(s)//2].lower()
        b = s[len(s)//2:].lower()
        for i in a:
            if i in 'aeiou':
                count += 1
        for j in b:
            if j in 'aeiou':
                count -= 1
        return count == 0
s = "AbCdEfGh"

print(Solution().halvesAreAlike(s))