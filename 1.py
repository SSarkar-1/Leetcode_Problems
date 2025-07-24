class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map={}
        for index,number in enumerate(nums):
            comp=target-number
            if comp in num_map:
                return [num_map[comp],index]
            num_map[number]=index
