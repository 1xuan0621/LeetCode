def topKFrequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)
    res = []
    for i in freq[::-1]:
        res.append(n)
        if len(res) == k:
            return res

nums = [5,3,1,1,1,3,73,1]
k = 2
print(topKFrequent(nums, k))