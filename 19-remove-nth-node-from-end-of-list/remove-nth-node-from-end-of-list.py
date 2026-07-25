# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt=0 ; temp=head
        while temp is not None:
            cnt+=1
            temp=temp.next
        res=cnt-n
        temp=head
        if cnt==n:
            return head.next
        while temp :
            res-=1
            if res==0:
                break
            temp=temp.next
            
        delNode=temp.next
        temp.next=temp.next.next
        delNode.next=None
        
        return head
        