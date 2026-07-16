# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fp=sp=head
        while fp is not None and fp.next is not None:
            fp=fp.next.next
            sp=sp.next

            if fp==sp:
                break

        else:
            return None

        fp=head 
        while fp is not sp:
            fp=fp.next
            sp=sp.next
        
        return fp