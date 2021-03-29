"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

-------------------
Constraints
1 <= prices.length <= 105
0 <= prices[i] <= 104
"""


def maxProfit(prices):
    profit, minimum = 0, 10000

    for price in prices:
        if price < minimum:
            minimum = price
        elif price - minimum > profit:
            profit = price - minimum
    return profit


prices = [7, 1, 5, 3, 6, 4]
# prices = [7,6,4,3,1]

print(maxProfit(prices))