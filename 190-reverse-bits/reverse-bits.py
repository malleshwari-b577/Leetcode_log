class Solution:
    def reverseBits(self, n: int) -> int:
        l=[]
        for _ in range(32):
            new=n%2
            l.append(str(new))
            n=n//2
        
        return int("".join(l),2)
