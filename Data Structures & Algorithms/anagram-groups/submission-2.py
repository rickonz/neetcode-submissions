class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # count char freq of each str --> how to store? 
        # --> {"010101..": ["str1", "str2"]}
        # group together == return dict values

        char_freq = defaultdict(list)
        for word in strs:
            freq = [0]*26
            for c in word:
                freq[ord(c)-ord('a')] += 1

            char_freq[tuple(freq)].append(word)

        return list(char_freq.values())

        