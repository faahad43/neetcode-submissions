class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        counter=1
        arrLen = len(nums)

        for idx in range(arrLen):
            if idx+1 == arrLen:
                res.append(counter) 
                continue
            res.append(math.prod(nums[idx+1 : arrLen]) * counter)
            counter *= nums[idx]
        return res

        