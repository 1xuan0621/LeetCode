def containsDuplicate(nums):
    new = set()
    for i in nums:
        if i in new:
            return True
        new.add(i)
    return False

print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))