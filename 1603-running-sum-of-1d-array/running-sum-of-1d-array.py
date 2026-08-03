class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        running_sum=0

        for i in range(len(nums)):
            running_sum+=nums[i]
            ans.append(running_sum)

        return ans