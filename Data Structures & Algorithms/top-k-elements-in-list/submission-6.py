class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the first k values that appear most frequently in the array
        # we need to first count all the values
        # then sort them by the amount of times they appear
        # then get the first `k` highest values

        # traverse array, counting the values in a dictionary
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        # sort the counts so that the largest are at the end of the array
        ordered_counts = sorted(counts.items(), reverse=False, key=lambda x: x[1])

        res = []
        while k > 0:
            # Pop the highest amount and append it to the result array until the k amount is reached
            val = ordered_counts.pop()[0]
            res.append(val)
            k -= 1
        
        return res
