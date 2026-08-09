class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for num in nums:
            temp=num
            digit=0
            while temp>0:
                rem=temp%10
                digit+=1
                temp//=10
            if digit%2==0:
                count+=1
        
        return count
