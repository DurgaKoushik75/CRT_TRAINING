stock_price = list(map(int , input().split()))
max_profit = 0
for buy in range(len(stock_price)):
    for sell in range(buy + 1 , len(stock_price)):
        profit = stock_price[sell] - stock_price[buy]
        if profit > max_profit:
            buy_day = buy + 1
            sell_day = buy + 1
            max_profit = profit
print("you can buy on Day ",buy_day,"and sell on Day",sell_day,"so you can  get max profit of",max_profit)            