def removeDuplicates(nums):
    new_nums = []
    for i in nums:
        if i not in new_nums:
            new_nums.append(i)
    for j in range(len(nums)-len(new_nums)):
        new_nums.append('_')

    return new_nums

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))