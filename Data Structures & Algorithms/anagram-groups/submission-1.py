class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets ={}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            signature = tuple(count)
            if signature not in buckets:
                buckets[signature] = []

            buckets[signature].append(word)
        return list(buckets.values())