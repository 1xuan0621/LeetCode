class Solution:
    def middleNode(self, head):
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr)//2]


head = [1,2,3,4,5]
print(Solution().middleNode(head))