# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fp=sp=head #keep two pointers 
        while fp and fp.next:
            fp=fp.next.next #fast pointer 2 steps
            sp=sp.next      #slow pointer 1 step

            #if fp and sp meets there is cycle
            if fp==sp:
                #reset one pointer to head other same node of intersection
                fp=head
                #when these two pointers meet then it is head 
                while fp is not sp:
                    fp=fp.next      #move each pointer 1 step
                    sp=sp.next
                return fp
        return None