import pickle

coins = 0
shop = {"atk": 0, "hp": 0, "crit": 0, "heal": 0, "armor": 0, "dodge": 0, "hcompanion": 0, "dcompanion":0}

pickle.dump(coins, open("game recode/coins.dat", "wb"))
pickle.dump(shop, open("shop.dat", "wb"))