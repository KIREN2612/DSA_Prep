'''Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       n = len(nums)
       #first we calculate the prefix
       prefix = [1] * n
       for i in range(1,n):
        prefix[i] = prefix[i-1] * nums[i -1] 
       #suffix part
       suffix = [1] * n
       for j in range(n-2,-1,-1):
        suffix[j] = suffix[j+1] * nums[j+1]

       result = [1] * n
       for k in range(n):
        result [k] = prefix[k] * suffix[k]
       return result
   
#Solution explanation:
#->this can be solved in a optimal way by using the prefix and suffix method
#->we first calculate the product of all the values from left to right which would be the prefix
#->next we calculate from right to left which would be the suffix
#->next we multiply them both to get the result