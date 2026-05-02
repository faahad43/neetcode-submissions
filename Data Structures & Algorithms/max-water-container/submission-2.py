class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l = 0 
        r = len(heights) - 1
        while l < r: 
            area = max(area, (r - l) * (min(heights[r], heights[l])))
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        return area
