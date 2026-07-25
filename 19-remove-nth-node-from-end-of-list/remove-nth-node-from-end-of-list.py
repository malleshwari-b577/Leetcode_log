# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        temp=sp=fp=head

        for _ in range(n):
            fp=fp.next

        if fp is None:
            return head.next

        while fp.next is not None:
            fp=fp.next
            sp=sp.next
    
        delNode=sp.next
        sp.next=sp.next.next
        delNode.next=None

        return head