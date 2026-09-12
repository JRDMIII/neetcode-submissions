class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # This will store all of the previous values we have seen
        prevMap = {}

        # loop through all the numbers
        for i, n in enumerate(nums):
            # we can calculate the difference between the current number and the target#
            # difference is also the complement
            diff = target - nums[i]
            
            # if the diff is already in the dictionary of previous differences
            if diff in prevMap:
                # we can use the index that is stored in that difference to solve the problem
                return [prevMap[diff], i]
            
            # otherwise, add the difference to the dictionary, with the index the difference is for
            prevMap[n] = i

        return [0, 0]