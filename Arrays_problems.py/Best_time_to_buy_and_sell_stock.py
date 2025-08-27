#LC 121
'''You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

#Code Solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')   # Initialize to a large number
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit >= max_profit:
                max_profit = profit
        return max_profit

#Code explanation:
#We use greedy algorithm for this problem:
'''Greedy algorithms are a class of algorithms that make locally optimal choices at each step with the hope of finding a global optimum solution.

At every step of the algorithm, we make a choice that looks the best at the moment. To make the choice, we sometimes sort the array so that we can always get the next optimal choice quickly. We sometimes also use a priority queue to get the next optimal item.
After making a choice, we check for constraints (if there are any) and keep picking until we find the solution.
Greedy algorithms do not always give the best solution. For example, in coin change and 0/1 knapsack problems, we get the best solution using Dynamic Programming.'''

#Here we use  greedy algorithm by first looping through the list and finding the min value first
#then we use the min value to subtract from the current price and set the profit
#we then compare the profit with the max_profit to get the maximum profit
