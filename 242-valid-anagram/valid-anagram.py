class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        visited={}
        for i in s:
            if i in visited:
                visited[i]+=1
            else:
                visited[i]=1
        for i in t:
            if i in visited:
                visited[i]-=1
            else:
                return False

        for val in visited.values():
            if val!=0:
                return False
        return True
