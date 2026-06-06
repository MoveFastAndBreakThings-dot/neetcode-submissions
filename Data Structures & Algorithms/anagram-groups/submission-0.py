class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = {}
        for word in strs:
            signature = "".join(sorted(word))
            if signature not in buckets:
                buckets [signature] = []

            buckets[signature].append(word)
        return list(buckets.values())
        