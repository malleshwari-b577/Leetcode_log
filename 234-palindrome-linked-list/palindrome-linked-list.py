# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack=[]
        temp=head

        #now traversal the LL and push in stack
        while temp:
            stack.append(temp.val)
            temp=temp.next

        #now re intilize the temp
        temp=head
        #now we will pop ele from stack and verify with LL
        while stack and temp:
            if stack.pop()!=temp.val:
                return False
            temp=temp.next
            
        return True