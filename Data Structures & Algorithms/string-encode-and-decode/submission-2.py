class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode as #<len><str>
        encoded = ""
        for string in strs:
            encoded = encoded + str(len(string)) + "#" + string

        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        i, decoded = 0, []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            l = int(s[i:j])
            i = j+1
            j = i+l
            string = s[i:j]
            decoded.append(string)
            i = j 
        
        return decoded


