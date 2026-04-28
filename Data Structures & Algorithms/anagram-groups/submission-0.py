class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ngramArray=[]
        lookupDic = {}
        if len(strs) == 1:
            return [strs]
        #run the loop for array length
        for i in range(len(strs)):
            if i in lookupDic:
                continue
            else:
                lookupDic[i] = strs[i]
            subsetArr = [strs[i]]
            #take in sequential manner item of array and 
            item = sorted(strs[i])
            for j in range(i+1, len(strs)):
                if len(item) != len(strs[j]):
                    continue
                if item == sorted(strs[j]):
                    subsetArr.append(strs[j])
                    lookupDic[j] = strs[j]
            ngramArray.append(subsetArr)
        return ngramArray

                




        