class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {value: index for index, value in enumerate(nums)}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums_dict and nums_dict[diff] != i:
                return [i, nums_dict[diff]]
        
        return []