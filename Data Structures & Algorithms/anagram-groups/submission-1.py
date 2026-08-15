class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Dictionary to hold the grouped anagrams
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the string to create a canonical key
            sorted_key = "".join(sorted(s))
            # Append the original string to its corresponding group
            anagram_map[sorted_key].append(s)
            
        # Return all the grouped lists
        return list(anagram_map.values())