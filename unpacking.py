# first, _ = input("What's your name? ").split(" ")
# print(f"hello, {first}")

# total converts a users galleons, sickles, and knuts into a total amount of knuts
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

# coins = [100, 50, 26]

# print(total(coins[0], coins[1], coins[2]), "Knuts")
# *coins will unpack the coins list 
# print(total(*coins), "Knuts")

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# use **coins to unpack the dictionary
print(total(**coins), "Knuts")