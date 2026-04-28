class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        res=[]
        arrLen= len(nums)
        lCounter = 1
        rCounter = 1

        for idx in nums:
            prefix.append(lCounter)
            lCounter *= idx

        for idx in reversed(nums):
            postfix.append(rCounter)  
            rCounter *= idx
        
        postfix.reverse()
        
        for  i in range(arrLen):
            res.append(prefix[i] * postfix[i])
        return res