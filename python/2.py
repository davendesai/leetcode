# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head

        carry = 0
        while l1 is not None or l2 is not None or carry > 0:
            val = 0
            if l1: 
                val += l1.val
            if l2:
                val += l2.val
            val += carry
        
            carry = val // 10
            val = val % 10

            node = ListNode(val)
            curr.next = node
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head.next
