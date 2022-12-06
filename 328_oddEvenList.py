class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        odd = head
        even = odd.next
        evenhead = even

        while even and even.next:
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = odd.next
        odd.next = evenhead
        
        return head