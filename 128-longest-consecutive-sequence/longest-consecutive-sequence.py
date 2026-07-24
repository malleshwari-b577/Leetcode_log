class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq=set(nums)
        long=0
        for i in freq:

            if i-1 not in freq:
                curr=i
                count=1

                while curr+1 in freq:
                    curr+=1
                    count+=1
                
                long=max(count,long)

        return long

