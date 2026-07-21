class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_count = {}
        win_count = {}

        # count s1 characters
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        # build first window
        for i in range(len(s1)):
            char = s2[i]
            win_count[char] = win_count.get(char, 0) + 1

        # check first window
        if win_count == s1_count:
            return True

        # slide the window
        for i in range(len(s1), len(s2)):

            # add new right character
            right_char = s2[i]
            win_count[right_char] = win_count.get(right_char, 0) + 1

            # remove old left character
            left_char = s2[i - len(s1)]
            win_count[left_char] -= 1
            if win_count[left_char] == 0:
                del win_count[left_char]      # clean up zeros

            # check if window matches s1
            if win_count == s1_count:
                return True

        return False
        