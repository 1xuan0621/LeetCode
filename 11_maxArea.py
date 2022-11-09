class Solution:
    def maxArea(self, height):
        maxa = 0
        l, r = 0, len(height) - 1
        while l < r:
            curv = min(height[l], height[r]) * (r - l)
            maxa = max(maxa, curv)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxa


height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))