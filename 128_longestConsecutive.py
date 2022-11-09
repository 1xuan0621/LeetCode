def longestConsecutive(nums):
    numset = set(nums)
    longest = 0

    for n in nums:
        if (n-1) not in numset:
            lenth = 0
            while (n+lenth) in numset:
                lenth += 1
            longest = max(longest, lenth)
    return longest
# nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))