class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arrLen = len(nums)
        for idx in range(arrLen):
            for num in range(idx+1, arrLen):
                if nums[idx] + nums[num] == target:
                    return [idx, num]
        

        