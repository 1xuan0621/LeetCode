class Solution:
    def threeSum(self, nums):
        ans = []
        nums.sort()

        for i, v in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l ,r = i+1, len(nums) - 1
            while l < r:
                if v + nums[l] + nums[r] > 0:
                    r -= 1
                elif v + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    ans.append([v, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return ans




nums = [-1,0,1,2,-1,-4]
output = [[-1,-1,2],[-1,0,1]]

print(Solution().threeSum(nums))