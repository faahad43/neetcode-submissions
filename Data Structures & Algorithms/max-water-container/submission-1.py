class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l = 0 
        r = len(heights) - 1
        while l < r:
            width =  r - l
            height = min(heights[r], heights[l])
            newarea = width * height
            area = max(area, newarea)
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        return area


        