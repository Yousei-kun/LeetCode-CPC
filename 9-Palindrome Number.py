class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool

        https://leetcode.com/problems/palindrome-number/

        HOW TO TACKLE THE PROBLEM:
        
        1. CAST the number to String

        2. ITERATE until HALF of the number's length (You don't need to check ALL of it)

           2.a -> IF the nth digit from left is not the same as the digit from nth right, return False

        3. IF False is not returned, return True

        """

        # Cast the number (Step 1)
        str_x = str(x)

        # Iterate until half (len(str_x)//2) (Step 2)
        for i in range(len(str_x)//2):

            # IF the nth left & right not equal, return False (Step 2.a)
            if str_x[i] != str_x[len(str_x)-1-i]:
                return False
        
        # IF false is not returned, return True (Step 3)
        return True