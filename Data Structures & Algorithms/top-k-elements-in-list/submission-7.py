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
        
        # we can use a min-heap to store all the elements, removing the smallest one everytime we exceed k numbers

        heap = []
        for n in counts.keys():
            # push the tuple to the heap, putting the count first so that can be used for ordering
            heapq.heappush(heap, (counts[n], n))
            
            # check if we have exceeded k values in the List
            if len(heap) > k:
                # if we have, pop the smallest value from the heap
                heapq.heappop(heap)
            
        # once all keys are iterated, the heap should only have the k highest values left
        return [v[1] for v in heap]