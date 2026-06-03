class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: If lengths don't match, they cannot be anagrams
        if len(s) != len(t):
            return False
            
        # Step 2: Create empty Hash Maps to store letter counts
        countS = {}
        countT = {}
        
        # Step 3: Count the characters in both strings
        for i in range(len(s)):
            # .get(character, 0) gives the current count, or 0 if it's a new letter
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        # Step 4: Compare both Hash Maps directly
        return countS == countT

# --- TEST EXECUTION ---
solver = Solution()

# Test case 1 (Should be True)
print("Is 'anagram' and 'nagaram' an anagram?", solver.isAnagram("anagram", "nagaram"))

# Test case 2 (Should be False)
print("Is 'rat' and 'car' an anagram?", solver.isAnagram("rat", "car"))
