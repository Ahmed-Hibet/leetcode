# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        parent = None
        root = None
        while l1 or l2:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            result = l1_value + l2_value + remainder
            node = ListNode(val=result%10)
            if parent:
                parent.next = node
            else:
                root = node
            parent = node
            remainder = result//10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        while remainder:
            node = ListNode(val=remainder%10)
            parent.next = node
            parent = node
            remainder //= 10
        return root
