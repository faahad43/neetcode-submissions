class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}
        for item in strs:
            sortedItem = "".join(sorted(item))
            if sortedItem not in lookup:
                lookup[sortedItem]= []
            lookup[sortedItem].append(item)
        
        return list(lookup.values())