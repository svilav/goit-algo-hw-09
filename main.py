import timeit


def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count

    return result


def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    last_coin = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin

    result = {}
    while amount > 0:
        coin = last_coin[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result


# Функції-обгортки для вимірювання часу виконання
def wrapper_greedy():
    return find_coins_greedy(113)


def wrapper_dp():
    return find_min_coins(113)


# Оцінка часу виконання
time_greedy = timeit.timeit(wrapper_greedy, number=1000)
time_dp = timeit.timeit(wrapper_dp, number=1000)

print(f"Greedy algorithm time: {time_greedy:.6f} seconds")
print(f"Dynamic programming algorithm time: {time_dp:.6f} seconds")

# Приклади використання:
print(find_coins_greedy(113))  # {50: 2, 10: 1, 2: 1, 1: 1}
print(find_min_coins(113))  # {50: 2, 10: 1, 2: 1, 1: 1}
