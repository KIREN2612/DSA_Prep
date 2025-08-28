'''Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Here it is 2 because the index 0 and 1 combined would give k[1,1] also index 1 and 2[1,1]
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
here the two would be [3] which gives k and also [1,2]

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        count = 0
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            count += seen.get(prefix_sum - k,0) #see if we have the remainder in the dictionary if yes add that to count or add 0
            seen[prefix_sum] = seen.get(prefix_sum,0) + 1
        return count
    
#Code explanation
#->Here we might think we can do this with the sliding window but here we only need the count and not the subarray
#->we first initialize the dictionary with 0 and 1 because it tells we have 1 count of having 0 which helps pass all cases
#->then we initalize the count and the prefix sum and here the prefix sum helps us solve this 
#->prefix_sum helps calculate the total of all values like [1,2,3] prefix_sum would be [1,3,6]
#->here then we store the values to seen if not already and if it already exists in seen we increase the count by the number of values from seen

