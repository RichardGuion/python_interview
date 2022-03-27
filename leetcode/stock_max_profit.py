import pytest


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    print('prices is: ' + ', '.join(str(x) for x in prices))
    if not prices:
        return 0
    index, profit = 0, 0
    while index < len(prices) - 1:
        try:
            while prices[index + 1] <= prices[index]:
                index += 1
        except IndexError:
            break

        buying_price = prices[index]
        while index < len(prices) - 1 and prices[index + 1] >= prices[index]:
            index += 1
        selling_price = prices[index]

        profit += selling_price - buying_price
        print(f'Taking profit {selling_price} - {buying_price} = profit {selling_price - buying_price}')
        index += 1
    print(f'final profit is: {profit}')
    return profit


@pytest.mark.parametrize("list_prices, expected_profit", [
    ([7, 1, 5, 3, 6, 4], 7),
    ([1,2,3,4,5], 4),
    ([7,6,4,3,1], 0)
])
def test_max_profit(list_prices, expected_profit):
    assert maxProfit(list_prices) == expected_profit


# def maxProfit(prices):
#     index = 0
#     last_index = len(prices) - 1
#     total_profit = 0
#     while index < last_index:
#         strike_price = prices[index]
#         if (index + 1) < last_index:
#             max_value = max(prices[index + 1:last_index])
#         else:
#             max_value = prices[last_index]
#         if max_value > strike_price:
#             total_profit += (max_value - strike_price)
#             print(f'buy at {strike_price}, sell at {max_value}, profit = {max_value - strike_price}')
#             index = prices.index(max_value)
#         else:
#             index += 1
#     return total_profit
#
#
# def maxProfit2(prices):
#     profit = 0
#     for i in range(len(prices) - 1):
#         if prices[i] <= prices[i + 1]:
#             profit += prices[i + 1] - prices[i]
#             print(f'maxProfit2 step {prices[i + 1]} - {prices[i]} = {profit}')
#     return profit
#
#
# maxp = maxProfit([7, 1, 5, 3, 6, 4])
# print(f'total profit is: {maxp}')
# maxp1 = maxProfit2([1,2,3,4,5])
# print(f'total profit is: {maxp1}')
#
# maxp2 = maxProfit2([7, 1, 5, 3, 6, 4])
# print(f'total profit 2 is: {maxp2}')
# maxp3 = maxProfit2([1,2,3,4,5])
# print(f'total profit 3 is: {maxp3}')
# maxp4 = maxProfit2([7,6,4,3,1])
# print(f'total profit 4 is: {maxp4}')