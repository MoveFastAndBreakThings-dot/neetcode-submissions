class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left    = 0
        max_len = 0
        max_freq = 0
        count   = {}                         # frequency of each char in window

        for right in range(len(s)):          # grow window to the right

            char = s[right]
            count[char] = count.get(char, 0) + 1            # add new char to window
            max_freq = max(max_freq, count[char])            # update max frequency

            replacements_needed = (right - left + 1) - max_freq  # chars to replace

            if replacements_needed > k:      # window invalid
                count[s[left]] -= 1         # remove leftmost char
                left += 1                   # shrink from left

            max_len = max(max_len, right - left + 1)  # update best length

        return max_len