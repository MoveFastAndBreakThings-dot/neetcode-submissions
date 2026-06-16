import time
import sys

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start_time = time.perf_counter()
        
        left = 0
        right = len(s) - 1
        initial_space = sys.getsizeof(left) + sys.getsizeof(right)

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                end_time = time.perf_counter()
                elapsed_time = end_time - start_time
                print(f"Time taken: {elapsed_time:.10f} seconds")
                print(f"Estimated space used: {initial_space} bytes (O(1) extra space)")
                return False

            left += 1
            right -= 1

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Time taken: {elapsed_time:.10f} seconds")
        print(f"Estimated space used: {initial_space} bytes (O(1) extra space)")
        return True