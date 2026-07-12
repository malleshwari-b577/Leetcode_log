class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x  ; rev=0
        while n>0:
            rem=n%10
            rev=(rev*10) + rem
            n=n//10
        return x==rev
