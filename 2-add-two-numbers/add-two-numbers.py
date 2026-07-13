# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        temp=dummy
        carry=0
        while l1 or l2 or carry!=0:
            t_sum=0
            #add if l1 is not none
            if l1 is not None:
                t_sum+=l1.val
                l1=l1.next
            #add if l2 is not none
            if l2 is not None:
                t_sum+=l2.val
                l2=l2.next
            #add carry
            t_sum+=carry
            carry=t_sum//10               #set carry if there
            new=ListNode(t_sum%10)    #now create new node

            #now creating answer ll with dummy poitnig to new sol
            temp.next=new
            temp=new

        return dummy.next