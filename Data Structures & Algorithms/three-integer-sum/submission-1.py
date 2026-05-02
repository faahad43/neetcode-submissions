class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res=[]
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while r > l:
                if nums[i] + nums[r] + nums[l] == 0:
                    if [nums[i],nums[r],nums[l]] not in res:
                        res.append([nums[i],nums[r],nums[l]])
                    l+=1
                    r-=1
                elif nums[i] + nums[r] + nums[l] > 0:
                    r-=1
                else:
                    l+=1
        return res
            
        