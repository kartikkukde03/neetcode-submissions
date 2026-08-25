class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        marea = 0
        while left < right:
            current_height = min(heights[left],heights[right])
            width = right - left
            area = current_height*width
            if area > marea:
                marea = area
            if heights[left] <heights[right]:
                left += 1
            else :
                right -= 1
        return marea

        