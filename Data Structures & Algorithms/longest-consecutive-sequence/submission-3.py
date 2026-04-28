class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        snums = sorted(set(nums))
        dic = {}
        counter = 1
        largest = 1
        for num in snums:
           value = dic.setdefault(num,0)
           dic[num] = value+1
        
        for num in snums:
            if num+1 in dic:
                counter+=1
            else:
                if counter > largest:
                    largest = counter
                counter=1
        return largest
                
        

        