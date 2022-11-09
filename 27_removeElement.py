def removeElement(nums, val):
    j = 0
    for i in nums:
        if i != val:
            nums[j] = i
            j += 1
    return j