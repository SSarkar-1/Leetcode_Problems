class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen={}
        l,r=0,min(k,len(nums)-1)
        for i,val in enumerate(nums):
            if val in seen and i-seen[val]<=k :
                return True
            seen[val]=i
        return False