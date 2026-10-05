class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        see=set()

        for i in nums:
            if i in see:
                return True
            else:
                see.add(i)
        
        return False