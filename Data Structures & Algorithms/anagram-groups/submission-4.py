class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we have an array of strings
        # we need to group all anagrams together into a List

        # two strings that are the same anagram will produce the same output when they are sorted
        # we can sort each string, and then use the sorted string as a dictionary key

        anagram_dict = defaultdict(list)

        # loop through all strings
        for s in strs:
            # sort the values within the string
            sorted_s = ''.join(sorted(s))
            # add the string to that sorted key
            anagram_dict[sorted_s].append(s)
        
        # return the list of dictionary values
        return list(anagram_dict.values())