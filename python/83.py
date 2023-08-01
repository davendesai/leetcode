# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        ret = curr = head
        while curr:
            nxt = curr.next
            if nxt and curr.val == nxt.val:
                curr.next = nxt.next
            else:
                curr = nxt
        return ret

