class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        ans=[]
        for chr in words:
            l=0 ; r=len(chr)-1 ; crt=list(chr) ; rev=crt
            while l<r:
                rev[r],rev[l]=rev[l],rev[r]
                l+=1
                r-=1
            rev=''.join(rev)
            print(chr,rev)
            if chr==rev:
                ans.append(chr)
                break

        return ''.join(ans)