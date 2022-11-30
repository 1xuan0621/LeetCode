class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        count = {}
        for i in arr:
            count[i] = 1 + count.get(i, 0)
        ans = len(set(count.values())) == len(list(count.values()))
        return ans



arr = [-3,0,1,-3,1,1,1,-3,10,0]

print(Solution().uniqueOccurrences(arr))