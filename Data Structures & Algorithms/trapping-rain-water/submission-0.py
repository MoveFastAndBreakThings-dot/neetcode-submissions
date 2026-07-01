class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total = 0

        left_max  = [0] * n          # left_max[i]  = tallest bar from 0 to i
        right_max = [0] * n          # right_max[i] = tallest bar from i to n-1

        # fill left_max going left to right
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])

        # fill right_max going right to left
        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        # now calculate water at each bar
        for i in range(n):
            water = min(left_max[i], right_max[i]) - height[i]
            total += max(0, water)

        return total