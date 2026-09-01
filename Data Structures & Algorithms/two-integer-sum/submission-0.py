class Solution:
    def twoSum(self, nums, target):
        seen={}
        for i,num in enumerate(nums):
            a=target-num
            if a in seen:
                return [seen[a],i]
            seen[num]=i

        