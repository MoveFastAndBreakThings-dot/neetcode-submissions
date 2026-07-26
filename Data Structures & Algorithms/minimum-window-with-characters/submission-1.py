class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

    # count characters needed from t
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        need = len(t_count)   # unique chars we must satisfy
        have = 0              # unique chars we currently satisfy

        win_count = {}        # counts in current window
        left = 0
        result = ""
        result_len = float('inf')

        for right in range(len(s)):

            # add new right character
            char = s[right]
            win_count[char] = win_count.get(char, 0) + 1

            # did we just satisfy a character from t?
            if char in t_count and win_count[char] == t_count[char]:
                have += 1

            # shrink from left while window is valid
            while have == need:

                # update result if this window is smaller
                if (right - left + 1) < result_len:
                    result_len = right - left + 1
                    result = s[left : right+1]

                # remove left character
                left_char = s[left]
                win_count[left_char] -= 1

                # did we lose a satisfied character?
                if left_char in t_count and win_count[left_char] < t_count[left_char]:
                    have -= 1

                left += 1

        return result
        