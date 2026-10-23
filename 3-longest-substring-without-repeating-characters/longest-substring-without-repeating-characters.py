class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        seen=set()
        left=0

        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
                max_len=max(max_len,right-left+1)
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left+=1
                seen.add(s[right])

        return max_len