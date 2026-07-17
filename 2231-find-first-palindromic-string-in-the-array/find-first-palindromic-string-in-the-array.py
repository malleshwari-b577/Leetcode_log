class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
    
        for chr in words:
            if self.isPalin(chr):
                return chr
        return ""

    def isPalin(self,word):
        l=0 ; r=len(word)-1
        while l<r:
            if word[l]!=word[r]:
                return False
            l+=1
            r-=1
        return True
