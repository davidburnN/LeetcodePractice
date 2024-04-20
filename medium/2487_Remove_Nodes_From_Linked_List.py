class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f'{self.val}'

class Solution:
    def removeNodes(self, head: list[ListNode]) -> list[ListNode]:
        def removeNodes(self, head: list[ListNode]) -> list[ListNode]:
            if not head:
                return None

            head.next = self.removeNodes(head.next)
            
            if head.next and head.val < head.next.val:
                return head.next
            return head
