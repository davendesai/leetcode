# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = tail = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                node = ListNode(list1.val)
                list1 = list1.next
            else:
                node = ListNode(list2.val)
                list2 = list2.next

            tail.next = node
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        # cut out the dummy head node we added 
        return head.next

