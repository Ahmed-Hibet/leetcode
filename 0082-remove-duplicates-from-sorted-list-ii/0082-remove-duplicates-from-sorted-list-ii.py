# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        duplicated = set()
        while current:
            if prev and current.val == prev.val:
                duplicated.add(current.val)
            prev = current
            current = current.next
        
        current = head
        result = None
        result_head = None
        while current:
            if current.val not in duplicated:
                if result: result.next = current
                else: result_head = current
                result = current
            elif result:
                result.next = None

            current = current.next

        return result_head
