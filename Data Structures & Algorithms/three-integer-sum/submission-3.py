class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        length = len(nums)
        for i, item in enumerate(nums):
            if i > 0 and item == nums[i-1]:
                continue
            l, r = i+1, length-1
            while l < r:
                Sum = nums[i] + nums[l] + nums[r]
                if Sum > 0:
                    r-=1
                elif Sum < 0:
                    l+=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        return res
                    



        