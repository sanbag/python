def buy_sell_stock(prices):
    min_p = float('inf')
    max_profit = 0

    for i in prices:
        min_p = min(min_p,i)
        profit = i-min_p
        max_profit =max(max_profit,profit)

    return max_profit

print(buy_sell_stock([7, 1, 5, 3, 6, 4]))