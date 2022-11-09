def searchInsert(nums: list[int], target: int):
    if target > nums[-1]:
        return len(nums)
    if target < nums[0]:
        return 0
    if target in nums:
        return nums.index(target)
    i, j = 1, len(nums) -2
    while i <= j:
        m = (i + j)  // 2   
        if nums[m] == target:
            return m
        elif nums[m] > target:
            j = m - 1
        else:
            i = m + 1
    return i
print(searchInsert(nums = [1,3,5,6], target = 7))