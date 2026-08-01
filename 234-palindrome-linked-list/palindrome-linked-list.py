# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev_ll(self,head):
        if head is None or head.next is None:
            return head

        new_head=self.rev_ll(head.next)

        forw=head.next

        forw.next=head

        head.next=None

        return new_head

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        sp=fp=head

        #find the middle
        while fp.next and fp.next.next:
            fp=fp.next.next
            sp=sp.next
        
        #reverse second half
        new_head=self.rev_ll(sp.next)

        #check first and second half
        first=head
        second=new_head

        #loop running
        while second:
            if first.val!=second.val:
                self.rev_ll(new_head)
                return False
            
            first=first.next
            second=second.next

        self.rev_ll(new_head)
        return True