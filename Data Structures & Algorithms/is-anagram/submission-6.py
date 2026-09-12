class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the two strings aren't the same length, the anagram can't be valid
        if len(s) != len(t): return False

        # count the number of times letters appear in s and t
        count_s, count_t = {}, {}

        for i in range(0, len(s)):
            # get the letter at index i in each string and update count
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        
        # go through every key in count_s
        for k, v in count_s.items():
            if count_t.get(k, None) != v: return False

        return True