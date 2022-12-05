class Solution:
    def minimumAverageDifference(self, nums) -> int:
        n = len(nums)
        total = sum(nums)
        avr_r = total
        total_l = 0
        min_dif = total
        ans = 0
        for i in range(n):

            total_l += nums[i]
            avr_r = total - total_l
            avr_l = total_l // (i + 1)

            if i != n - 1:
                avr_r //= (n - i - 1)
            dif = abs(avr_l - avr_r)
            if dif < min_dif:
                min_dif = dif
                ans = i
        return ans



nums = [2,5,3,9,5,3]
print(Solution().minimumAverageDifference(nums))