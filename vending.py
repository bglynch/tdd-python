from byotest import * 

# SAMPLE IMPORTED TDD -----------------------------------------------------------
# def double(n):
#     return n*2
    
# def increment(x):
#     return x + 1


# test_are_equal(double(2),4)
# test_greater_than(increment(3),3)

# VENDING MACHINE ---------------------------------------------------------

# from byotest import *

# eur_coins = [200, 100, 50, 20, 10, 5, 2, 1]
# usd_coins = [25, 10, 5, 1]

# def get_change(amount, coins=eur_coins):
#     change = []
#     for coin in coins:    
#         while amount >= coin:
#             amount -= coin
#             change.append(coin)
#     return change
    
# test_are_equal(get_change(0), [])  
# test_are_equal(get_change(1), [1])  
# test_are_equal(get_change(2), [2])
# test_are_equal(get_change(3), [2, 1])
# test_are_equal(get_change(7), [5, 2])
# test_are_equal(get_change(4), [2, 2])

# test_are_equal(get_change(80, usd_coins), [25, 25, 25, 5])


# print("All tests pass")



#VENDING MACHINE WITH LIMITED COINS ---------------------------------------------------------------

# Change the function so that instead of a list of coins, the function works with a dictionary that contains the coin denominations, and the quantity of each coin available. 
# By default assume there are 20 of each coin, but this can be overridden by passing a dictionary to the function as with the previous example.
# If a coin that would normally be used to make change isn't available the program should attempt to use smaller coins to make up the change.
# If it is not possible to make the change with the coins available, the function should raise an error.


eur_coins = {200:20, 100:20, 50:20, 20:20, 10:20, 5:20, 2:20, 1:20}
usd_coins = [25, 10, 5, 1]

def get_change(amount, coins=eur_coins):
    
    denominations = list(coins.keys())
    denominations.sort(reverse=True)
    
    change = []
    for coin in denominations:    
        while amount >= coin and coins[coin]>0: #and we have that coin:
            amount -= coin
            coins[coin] = coins[coin] - 1#and decrease amout of coint
            change.append(coin)
    return change
    
test_are_equal(get_change(0), [])  
test_are_equal(get_change(1), [1])  
test_are_equal(get_change(2), [2])
test_are_equal(get_change(3), [2, 1])
test_are_equal(get_change(7), [5, 2])
test_are_equal(get_change(4), [2, 2])
test_are_equal(get_change(55, { 50: 0, 20:20, 10: 20, 5: 20, 2: 20}), [20, 20, 10, 5])

# test_are_equal(get_change(80, usd_coins), [25, 25, 25, 5])


print("All tests pass")


