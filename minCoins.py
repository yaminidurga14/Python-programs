def min_coins(value,denominator):
    denominator.sort(reverse=True)
    result=[]
    for coin in denominator:
        while value>=coin:
            value-=coin
            result.append(coin)
    return len(result),result

value = 70
denominations = [50, 20, 10, 5, 2, 1]  # Common denominations
num_coins, coins_used = min_coins(value, denominations)
print(f"Minimum coins: {num_coins}")
print(f"Coins used: {coins_used}")