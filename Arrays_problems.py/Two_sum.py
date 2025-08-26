#LC-1
'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # stores num -> index
        for i,num in enumerate(nums):
            rem = target - num
            if rem in seen:
                return [seen[rem],i]
            seen[num] = i

#Solution Explanation:
'''We start with creating a empty dictionary to store the seen values
   Then start by looping through the list as we need to keep count of both value and the index we can use enumerate
   subtract the target from the number to get the reminder 
   check if the remainder exist in the list if yes then return the value or else move to the next
'''

