class Solution:
    def topKFrequent(self, nums,k):
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        bucket=[[] for _ in range(len(nums)+1)]
        for n,f in freq.items():
            bucket[f].append(n)
        ans=[]
        for b in bucket[::-1]:
            ans+=b
            if len(ans)>=k:
                return ans[:k]
        