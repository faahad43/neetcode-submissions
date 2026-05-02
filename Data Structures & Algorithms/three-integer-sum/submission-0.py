class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res=[]
        for i in range(len(nums)):
            r = i+1
            l = len(nums)-1
            while l > r:
                if nums[i] + nums[r] + nums[l] == 0:
                    if [nums[i],nums[r],nums[l]] not in res:
                        res.append([nums[i],nums[r],nums[l]])
                    r+=1
                    l-=1
                elif nums[i] + nums[r] + nums[l] > 0:
                    l-=1
                else:
                    r+=1
        return res
            
        