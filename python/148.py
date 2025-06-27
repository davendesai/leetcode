# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted = []
        
        curr = head
        while curr is not None:
            sorted.append((curr.val, curr))
            curr = curr.next
        sorted.sort(key=lambda val: val[0])
    
        dummy = ListNode()
        curr = dummy
        for _, node in sorted:
            node.next = None
            curr.next = node
            curr = curr.next

        return dummy.next
"""
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head

        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        def merge(l1: ListNode, l2: ListNode) -> ListNode:
            dummy = ListNode()
            curr = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next

            if l1:
                curr.next = l1
            elif l2:
                curr.next = l2
            return dummy.next

        return merge(left, right)
