
def twoSum(nums, target):
    # """
    # :type nums: List[int]
    # :type target: int
    # :rtype: List[int]
    # """
    seen = {}
    for i, value in enumerate(nums):
        remain = target - value
        if remain in seen:
            return [seen[remain],i]
        else:
            seen[value] = i

print(twoSum(nums = [3,3], target = 6))

