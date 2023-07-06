class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        You are given an array prices where prices[i] is the price of a
        given stock on the ith day. You want to maximize your profit by
        choosing a single day to buy one stock and choosing a different day
        in the future to sell that stock.

        Return the maximum profit you can achieve from this transaction.
        If you cannot achieve any profit, return 0.
                :type prices: List[int]
                :rtype: int
        """
        if len(prices) <= 1:
            return 0

        buy = 0
        sell = 1
        profit = 0

        while buy < len(prices) - 1:
            current_profit = prices[sell] - prices[buy]
            profit = max(profit, current_profit)
            if sell == len(prices) - 1:
                buy += 1
                sell = buy
            elif prices[buy] >= prices[sell]:
                buy = sell
            sell += 1

        return profit
