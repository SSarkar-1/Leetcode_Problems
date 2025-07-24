class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for val in nums:
            nums.remove(val)
        return len(nums)