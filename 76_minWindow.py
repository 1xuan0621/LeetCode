class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        l = 0
        min_window = len(s)
        count_t = {}
        matches = 0
        ans = ''
        for i in t:
            count_t[i] = 1 + count_t.get(i, 0)

        for r in range(len(s)):
            if s[r] in t:
                count[s[r]] = 1 + count.get(s[r], 0)
                if count[s[r]] == count_t[s[r]]:
                    matches += 1

            print(s[l], s[r], count, matches, ans)
            while matches == len(count_t.keys()):
                if r - l <= min_window:
                    ans = s[l:r+1]
                    min_window = r - l
                if s[l] in t:
                    count[s[l]] -= 1
                    if count[s[l]] < count_t[s[l]]:
                        matches -= 1
                l += 1


        return ans


s = "bbaa"
t = "aba"

print(Solution().minWindow(s, t))