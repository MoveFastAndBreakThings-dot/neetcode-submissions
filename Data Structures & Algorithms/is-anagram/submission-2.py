from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Counter(s) creates a Hash Map of character frequencies for string s
        # Counter(t) creates a Hash Map of character frequencies for string t
        # Python lets you compare these two maps directly using '=='
        return Counter(s) == Counter(t)


# --- EXECUTION CODE ---

# 1. Create an instance of the Solution class
solver = Solution()

# 2. Test Case 1: True Anagrams
word1 = "anagram"
word2 = "nagaram"
result1 = solver.isAnagram(word1, word2)
print(f"Are '{word1}' and '{word2}' anagrams? -> {result1}") 
# Output will be: True

# 3. Test Case 2: Not Anagrams
word3 = "rat"
word4 = "car"
result2 = solver.isAnagram(word3, word4)
print(f"Are '{word3}' and '{word4}' anagrams? -> {result2}") 
# Output will be: False
