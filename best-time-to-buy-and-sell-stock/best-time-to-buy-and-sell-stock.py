class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_time, buy_time_idx = prices[0], 0
        max_profit, sell_time_idx = 0, 0
        for i, price in enumerate(prices[1:]):
            if price < buy_time:
                buy_time = price
                buy_time_idx = i+1

            if price-buy_time > max_profit:
                max_profit = price-buy_time
                sell_time_idx = i+1
        
        return max_profit