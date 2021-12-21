"""
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a
    different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction.
    If you cannot achieve any profit, return 0.

    Constraints:
        1 <= len(prices) <= 10**5
        0 <= prices[i] <= 10**4
"""


def best_time_to_buy_and_sell_stock(prices):
    """Single pass O(N)"""
    max_profit = 0
    min_price = 10 ** 4 + 1
    for price in prices:
        if min_price > price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
