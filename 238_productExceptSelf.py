def productExceptSelf(nums):
    res = [1] * len(nums)
    pre = 1
    for i in range(len(nums)):
        res[i] = pre
        pre *= nums[i]
    post = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= post
        post *= nums[i]
    return res
nums = [1,2,3,4]
print(productExceptSelf(nums))