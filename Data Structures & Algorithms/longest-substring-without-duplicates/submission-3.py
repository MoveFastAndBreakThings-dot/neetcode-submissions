class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
            left    = 0
            max_len = 0
            window  = set()              # characters currently in our window

            for right in range(len(s)):  # expand right pointer every step

                while s[right] in window:       # duplicate found
                    window.remove(s[left])      # shrink from left
                    left += 1                   # move left forward

                window.add(s[right])            # add new character to window

                max_len = max(max_len, right - left + 1)  # update best length

            return max_len