import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        # count = {}
        # str_builder = []
        # for i in s:
        #     count[i] = 1 + count.get(i, 0)
        # sorted_list = sorted(count.items(), key=lambda x:x[1], reverse=True)
        # for n in sorted_list:
        #     ans += n[0]*n[1]
        
        # return ans

        counts = collections.Counter(s)
        str_builder = []
        for letter, freq in counts.most_common():
            str_builder.append(letter*freq)
    
        return ''.join(str_builder)
s = "Aabb"

print(Solution().frequencySort(s))