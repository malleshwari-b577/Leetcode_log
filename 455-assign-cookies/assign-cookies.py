class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count=0
        g.sort() ; s.sort()

        child=0 ; cook=0

        while child <len(g) and cook < len(s):
            if g[child]<=s[cook]:
                count+=1
                child+=1 
                cook+=1
            else:
                cook+=1

        
        return count