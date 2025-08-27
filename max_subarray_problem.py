#LC - 53
'''Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104'''

#Code Solution - Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sub_sum = float('-inf')
        sum_array = 0

        for num in nums:
            sum_array += num
            largest_sub_sum = max(sum_array,largest_sub_sum)
            if sum_array < 0:
                sum_array = 0
        return largest_sub_sum
    
#Explanation:
#We go with the Kadane's algorithm for this problem
#Kadane's Algorithm is an efficient method for finding the maximum sum of a contiguous subarray within a one-dimensional array of numbers, operating in linear time 
#here we loop through the list and take the sum through prefix_sum
#check and assign to largest if its greater than largest
#if the sum goes below 0 reset it to 0 so that the negative numbers dont affect 
