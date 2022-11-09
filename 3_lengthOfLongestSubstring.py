class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        l ,r = 0, 0
        m = 0
        while r < len(s):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            m = max(m, r - l + 1)
            r += 1
        return m
s = "dvdf"

print(Solution().lengthOfLongestSubstring(s))