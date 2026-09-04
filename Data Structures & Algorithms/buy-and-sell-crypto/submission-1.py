class Solution:
    def maxProfit(self, prices):
        profit=0
        buy=prices[0]

        for price in prices:
            if buy>price:
                buy=price
            else:
                profit=max(profit,price-buy)
        return profit
        