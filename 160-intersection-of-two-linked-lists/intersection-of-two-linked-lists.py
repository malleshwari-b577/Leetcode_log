# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        t1=headA
        t2=headB

        #check if both pointers point same node or not 
        while t1 is not t2:
            t1=t1.next if t1 is not None else headB
            t2=t2.next if t2 is not None else headA
        return t1