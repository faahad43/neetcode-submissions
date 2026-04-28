class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkArr= set()
        for num in nums:
            hasDup = num in checkArr
            if hasDup:
                return True
            checkArr.add(num)
        return False
        