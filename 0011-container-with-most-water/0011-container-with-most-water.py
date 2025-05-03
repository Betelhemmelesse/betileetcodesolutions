class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right,maxarea,n = 0,len(height)-1,0,len(height)
        while left <= right:
            x = min(height[left],height[right])
            area = x * (right - left)
            if area > maxarea:
                maxarea = area
            if x is height[left]:
                left += 1
            else:
                right -= 1       
        return maxarea   
        