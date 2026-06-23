class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left  = 0                    # start at beginning
        right = len(heights) - 1     # start at end
        max_water = 0                # track best so far

        while left < right:          # stop when they cross

            width  = right - left                        # distance between them
            height = min(heights[left], heights[right])  # shorter bar
            water  = width * height                      # water this container holds

            max_water = max(max_water, water)  # update best

            if heights[left] < heights[right]:  # left is shorter
                left += 1                       # move left inward
            else:                               # right is shorter (or equal)
                right -= 1                      # move right inward

        return max_water
            