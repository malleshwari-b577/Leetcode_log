# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy=ListNode(0,head)  #take dummy to handle edge cases

        fp=sp=dummy

        for _ in range(n+1):    #tkae fp. n+1 steps ahead
            fp=fp.next

        #now iterate till end
        while fp:
            fp=fp.next
            sp=sp.next

        #now deletion
        delNode=sp.next         #store deleting node
        sp.next=sp.next.next    #put sp.next to node next to delnode
        delNode.next=None

        return dummy.next