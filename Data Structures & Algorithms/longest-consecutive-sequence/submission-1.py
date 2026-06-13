class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashed = set(nums)
        longest_consec = 0
        for num in hashed:
            if (num - 1) not in hashed:
                current_num = num
                current_consec = 1
                while (current_num +1) in hashed:
                    current_num +=1
                    current_consec+=1
                longest_consec = max(longest_consec, current_consec)
        return longest_consec        