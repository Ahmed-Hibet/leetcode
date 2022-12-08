# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 1
        current = head
        while current.next:
            current = current.next
            counter += 1
        counter //= 2
        for i in range(counter):
            head = head.next
        return head
