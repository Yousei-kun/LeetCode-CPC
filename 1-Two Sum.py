class Solution(object):
    def twoSum(self, nums, target):
        """

        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        https://leetcode.com/problems/two-sum/

        HOW TO TACKLE THE PROBLEM:
        1. CREATE a dict to store the wanted value
           (ex: target is 9, current val is 2, so the wanted value is 7 (9-2))
           store 7 as the key, and the index as value to be returned later.

        2. ITERATE using enum to get BOTH index and value of the nums

           2.a -> IF we get the wanted value (ex: we get 7 from the 1st step)
                  return both the stored index of 2, and the newly traversed index of 7

           2.b -> IF there isn't the wanted value in the dict, add the new value to the dict.

        """

        # CREATE the new dict (Step 1)
        help_dict = {}

        # Start ITERATING (Step 2)
        for i, val in enumerate(nums):

            # Check if we get the wanted item (Step 2.a)
            if target-val in help_dict:
                val1 = help_dict[target-val] # the stored value
                val2 = i # the current index
                return [val1, val2]

            # Add the new value to the dict (Step 2.b)
            help_dict[val] = i
            
            
        