class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Format: length + delimiter + string
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Move j until we find the delimiter
            while s[j] != '#':
                j += 1
                
            # Extract the length of the string
            length = int(s[i:j])
            
            # Extract the actual string using the length
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            
            # Jump the pointer past the processed string
            i = j + 1 + length
            
        return res
