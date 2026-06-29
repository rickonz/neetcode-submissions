class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # The idea is we only care about the frequency of the characters in each word, so as to group them together into words with the same frequency of characters. 
        # Therefore, we can create a hash map, essentially a mapping to represent the frequency of the character map to the word. 
        # And return the massive group of words of those who have the same frequency of characters. 

        # We will use an array of length 26 to represent the frequency of each character. 
        # So, the pseudocode will be: we start with an empty hash map and we iterate through the strings. For each string, we increment the counts of the index of each character in the word and update the hash map of this frequency string with a value of this word. 
        # And in the end, we will have a hash map of the keys to be all the frequency strings and corresponding values of the words that map to those frequency strings. 
        # And therefore we only need to iterate through the hash map values to return them as a  group. 

        freq_table = {}
        for word in strs:
            freq_array = [0]*26
            for char in word:
                idx = ord(char)-ord('a')
                freq_array[idx] += 1

            
            freq_table.setdefault(tuple(freq_array), []).append(word)

        return list(freq_table.values())

